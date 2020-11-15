# Le Polyglotte

## Description

Nous avons intercepté un fichier top secret émanant d'Evil Country, il est très certainement en rapport avec leur programme nucléaire. Personne n'arrive à lire son contenu.

Pouvez-vous le faire pour nous ? Une archive était dans le même dossier, elle peut vous servir

## The First Message

First of all, [message.pdf](./message.pdf) is very hard to open. As far as we are aware, only Firefox was able to show something. Only the text `Top Secret` is visble. However you can either check in the inspector or select all the text and you will find the following message:

"Ce document concerne l operation soleil atomique. Cette operation est strictement confidentielle et ne doit en aucun cas etre devoilee.  Les informations sur l operation sont disseminees dans ce fichier. Chaque partie de l information est identifiee par un nombre par ex :  [0]ae7bca8e correspond a la premiere partie de l information qu il faut concatener au reste."

This message states that we need to search the PDF for every information one can found.

*__Note__: This message can aslo be found by decoding the stream of the text object present at the line 72 in the PDF.*

## Finding `[0]`

Opening the PDF in a text editor shows these first lines:
```html
<%PDF-1.2
<html>
<!DOCTYPE html>
<html>
  <head>
    <title>Flag</title>
    <meta charset="utf-8">
  </head>
<body>
<script>var flag = [91,48,93,97,97,57,51,56,97,49,54];</script>
<!--
```
Decrypting this returns code `[0]aa938a16`:
```javascript
var flag = [91,48,93,97,97,57,51,56,97,49,54];
decoded = String.fromCharCode.apply(String, flag);
console.log(decoded);
// [0]aa938a16
```

## Finding `[1]`

A PDF is ensentially structured like a tree. To simplify, when loading this page, it will call the object with id `2`. Then `2` is loading the object `4` and its children. However, there exists another object `3` that is never loaded. When changing `<< /Pages 4 0 R >>` to `<< /Pages 3 0 R >>` at line 14, another page will load with the code `[1]4d862d5a`.

*__Note__: This code can also be found in an object's data stream at line 46.*

## The Dead End

This is how the PDF is shown by default:
<p align="center">
    <img width=25% src="./message_pdf.png" alt="PDF">
</p>
As everyone can see, it seem to contains vertical lines. We fully thought that this was anamorphic text. Crushing it down to a notmal size, it seemed to be a very pixelated stream of 0s and 1s. We tried hours to decode this stream, to no avail. That's because these are not 0s nor 1s. These are the characters of the hidden message stretched vertically. This really blocked us for a very long time.

## Finding (?) `[3]` And Trailing Data

As shown earlier, the file has html tags. Opening it as a webpage shows us an alert with the text `_4aee=7<e5:`. It is just `[0]aa938a16` modified. This is the script that was executed:
```javascript
var flag = [91,48,93,97,97,57,51,56,97,49,54];
for(i=0;i<flag.length;i++){flag[i] = flag[i]+4} alert(String.fromCharCode.apply(String, flag));
```

Without knowing what to do with it (it does not unlock [secrets.zip](./secrets.zip)), we googled it. Interestingly, we landed on [ddecode.com](http://ddecode.com/hexdecoder/?results=71062843c5cd79a6c544e69b2525c63a) with the following text:
```
key='\xce]`^+5w#\x96\xbbsa\x14\xa7\x0ei'
iv='\xc4\xa7\x1e\xa6\xc7\xe0\xfc\x82'
[3]4037402d4
_4aee=7<e5:
```
It seemed like we found code `[3]4037402d4` but is is 12 characters instead of 11 like the others. Another thing are the `key` and `iv` values. `key` is 16 bytes whereas `iv` is only 8 bytes. This is the data needed to encrypt and decrypt with the [Triple DES](https://en.wikipedia.org/wiki/Triple_DES) method.

Another thing that was spotted is the trailing data in the PDF. After `</html><!--`, there is byte `\0x06` repeated 6 times and data just after. Weirdly, if we remove these first 6 bytes, the data has the right length to be decoded with Triple DES. The data starts at offset `0x9a0 = 2464`. With [3DES-decrypt.py](./3DES-decrypt) (Requires [pyDes.py](https://gist.github.com/eigenein/1275094)), we can decrypt it.

```
$ tail -c +2465 message.pdf > raw
$ python 3DES-decrypt.py raw decr
$ file decr
decr: DOS executable (COM)
```

We then tried to execute the file on a DOS emulator. It sadly did not work.

## secrets.zip

Finally, we have the file [secrets.zip](./secrets.zip). It contains an image and a text file. However, we are unable to unzip these files without knowing the password beforehand. We tried to bruteforce the password with zip2john and john but, due to a lack of experience with these tools and our limited time, we were not able to crack it.