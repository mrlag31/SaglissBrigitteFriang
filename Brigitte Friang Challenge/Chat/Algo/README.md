# Algo

## Evil Gouv Recrute

In this challenge, Blaise Pascal tells us he was able to intercept a modified file ([original.txt (original)](./original.txt), [intercepte.txt (modified)](./Evil%20Group%20Recrute/intercepte.txt)) and a message is probably hidden in the later. These are the first lines of each file:
```
original.txt:
    HEALTH ASPECTS

    OF
    CHEMICAL AND BIOLOGICAL

intercepte.txt:
    HbEALTH ASPECTS

    aOF 
    CsHEMIeCAL6 AND4 BIOLOGICAL:
```
One can now assume that the intercepted file is the same as the original one, except that new characters have been added. The script [diff_extract.py](./Evil%20Group%20Recrute/diff_extract.py) will do just that.
```
$ python diff_extract.py diff.txt
```
This will extract all of the extra characters and save them in [diff.txt](./Evil%20Group%20Recrute/diff.txt). It is mostly gibberish except for the first few characters: `base64:`. This indicates that the file is encoded in Base 64. Using `base64` or [decode_base64.py](./Evil%20Group%20Recrute/decode_base64.py), we can decode the file.
```
$ tail -c +8 diff.txt | base64 -d > raw
$ python decode_base64.py diff.txt raw
```
We can then use `file` to check for its type. This can also be done by opening the file in a HexEditor and searching for magical number (`JFIF` in our case, which is a JPEG format)
```
$ file raw
raw: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, progressive, precision 8, 596x842, components 3
```
Here is what the image looks like:

<p align="center">
    <img width=20% src="./Evil Gouv Recrute/raw" alt="raw shown as an image">
</p>

We can now extract a new link from this image: https://www.challengecybersec.fr/22caeee05cb8b2a49133be134a5e9432

*__Note__: At first, we thought that `/22caeee05cb8b2a49133be134a5e9432` was in upper case, like in the image. However, https://www.challengecybersec.fr/22CAEEE05CB8B2A49133BE134A5E9432 responded with a 404 and it took us a long time to find out what was the issue.*

## Knapsack

When getting to the last URL, we are prompted to resolve an internal problem about storing things in a warehouse. Reading [IMPORTANT.pdf](./Knapsack/IMPORTANT.pdf), we can determine that it is a slightly modified version of the [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem).

The [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem) is a well-known NP-problem that consists in packing the most value with a maximum weight. Let's take an example: imagine you are a thief and can only transport 20kg maximum. When entering the house, you spot 3 objects that weight 16, 11 and 5kg and are valued at 100, 60 and 32€ respectively. The Knapsack problem is to find which objects to take to maximise our backpack value while not going over the maximum weight.

This is how it is usually resolved. Let `n` be the number of objects, `M` be the max weight, `W = {w1, ..., wn}` the weights and `V = {v1, ..., vn}` their values (`V = W` for our problem). We suppose the weights and the values are all positive and different. Let also define `S(i, j)` the solution of the problem with the first `i`-th objects and a maximum weight of `j`. The value of our backpack solution is `S(n, M)`.

We need to find a relation between `S(i,j)` and `S(i-1, j')`. First, `S(0, j) = 0` is obvious, the value of an empty backpack will always be 0. Now, let `I` be the set of object indices for the maximum solution of `S(i, j)`. If `i in I` then `S(i, j) = S(i-1, j-wi) + vi` (with `I\{i}` the set of object indices for the maximum solution of `S(i-1, j-wi)`) else `S(i,j) = S(i-1,j)`. To know if `i in I`, we only need to check which one is greater between `S(i-1,j)` and `S(i-1, j-wi) + vi`. To summarize, `S(i, j)` can be calculated like this:

```
          | 0                                if i = 0
S(i, j) = | S(i-1, j)                        if wi > j
          | max(S(i-1, j), (i-1, j-wi) + vi) else
```

How is it implemented for this problem? A purely recurrent function is possible, used in [rec.py](./Knapsack/rec.py) it has very low memory usage but horrible performance. It is usually done using [dynamic programmation](https://en.wikipedia.org/wiki/Dynamic_programming), where we store intermediate data (in a dictionnary for space)) but still uses a recurrent function, used in [dyn.py](./Knapsack/dyn.py). Recurence can be an issue with large set of data because it may hit the end of the limits of reccurence. It is thus implemented with a pile where elements in the pile have not been calculated yet. It is implemented in [pil.py](./Knapsack/pil.py).

```
$ python rec.py fichier_a_petit.in 
200

$ python dyn.py fichier_a_petit.in
200

$ python pil.py fichier_a_petit.in
200
```

Sadly, either due to our inability to spot the subtility of this problem or the slowness of python, we were not able to complete this challenge.

*__Note__: Although it is not discussed here, it is possible to recover `I` from the results of `S(i, j)` by checking, starting from `n` down to `1`, if `S(i, j) = S(i-1, j)` or not. Math is shown as code because GitHub doesn't support LaTeX or KaTeX yet.*