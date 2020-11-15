# Keypad Sniffer

## Description

Le code d'accès d'un centre militaire de télécommunications est saisi sur un clavier. Un agent a accédé au matériel (Cf. photos face avant et face arrière du clavier) et a inséré un dispositif pour enregister les données binaires qui transitent sur le connecteur du clavier. Le fichier joint (keypad_sniffer.txt) comprend les données binaires (échantillonnées à une fréquence de 15 kHz) au moment où une personne autorisée rentrait le code d'accès. Retrouvez le code d'accès.

## Available Data

For this challenge, we know that someone put a sniffer on a keypad. We have these 2 images showing the front and the back of the keypad with the sniffer:

<p align="center">
    <img width=25% src="./keypad_face.jpg" alt="keypad_face">
    <img width=25% src="./keypad_back.jpg" alt="keypad_back">
</p>

We also have the siffed data.

## Search

### How keypads work ?

Before that, we never worked with a keypad. After some research we discovered that it's pretty simple and it's just a multiplexing of columns and rows.

For the microcontroller, it's not highly complex either: 

- Columns are output ( low level at start )
- Rows are input ( high level at start )

Then to detect which key is pressed, the controller scan in loops each column by setting it to high value. If a row is at high value then we know which column and which row and then the key. 

### Wiring

Now that we know how it works, we need to figure out what each bit in our file is related to. We have a 4x4 keypad so we are supposed to have 8 usd bits but our file contain 12.

Here are the first lines in the file with the 4 last bits put in evidence:
```
10111110 0111
10111110 0111
10111110 0111
10111110 0111
10111110 0111
10111110 0111
10111110 0111
10111110 0111
10111110 1011
10111110 1011
10111110 1011
10111110 1011
10111110 1011
10111110 1011
10111110 1011
10111110 1011
10111110 1101
10111110 1101
10111110 1101
10111110 1101
10111110 1101
10111110 1101
10111110 1101
10111110 1110
10111110 1110
10111110 1110
10111110 1110
10111110 1110
10111110 1110
10111110 1110
```
We can easily see a part that seems to be the scan part. So this 4 bits are useful. We also check in the rest of the file that bits `[0:1]` and `[7:8]` never change which correlates to the welded pins.

So, we know that bits `[2:6]` are inputs and `[9:12]` are for the scan. However, we do not know where are these bits connected to.

## Solve

Now we know how the keypad works, let's implement that in a script. To simplify this part we first removed bits `[2:6]` and `[9:12]` from the file. We also need to find how the keypad is wired. So we test the password for each of the 8 possible wiring combinations.

```
$ python resolve.py output.txt
DGSESIEE{F036A55C888D47E11942}
DGSESIEE{C4D9166A555032BFF83E}
DGSESIEE{A308F9916664DE7CC5DB}
DGSESIEE{1D45C88F99930B2AA607}
DGSESIEE{1B25C66A9997ED4FF8E3}
DGSESIEE{AE78F55C666B23011924}
DGSESIEE{C2B9188F555E74DAA670}
DGSESIEE{F7E6A9918882B03CC5BD}
```

By testing every pass, we found out that `DGSESIEE{AE78F55C666B23011924}` was the right one and claim these 150 points.

*__Note__: The sniffed data is not present because it is over 5MB.*