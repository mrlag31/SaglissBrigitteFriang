# Définition

## Description

 Un de vos collègues a créé un petite énigme, il est un peu lourd et vous demande depuis des semaines de la résoudre, faites lui plaisir. Voici l'énigme : Quelle heure est-t-il ?

Connectez-vous via `nc challengecybersec.fr 6660`

## Challenge

In this challenge, we only have the clue "Quelle heure est-t-il ?" / "What time is it ?". And we know that we have to connect via ``nc challengecybersec.fr 6660``. 

## Solution

At the begin we simply tried the command, here is the output :

```
$ nc challengecybersec.fr 6660
Entrez la reponse ( Enter reply ) : 
 > now
 > Mauvaise reponse !
```

Then we were pretty sure we need to type actual time in the prompt. But, in which format ? After différent tries we found that it was in UNIX Epoch time.

```
$ date "+%s" | nc challengecybersec.fr 6660
 > Entrez la reponse :
 > Bravo ! Voici le flag : DGSESIEE{cb3b3481e492ccc4db7374274d23c659}
```

We can then use this flag and claim those 50 points.