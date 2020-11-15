# Définition

### Challenge

In this challenge, we only have the clue "Quelle heure est-t-il ?" / "What time is it ?". And we know that we have to connect via ``nc challengecybersec.fr 6660``. 

### Resolve

At the begin we simply tried the command, here is the output :

``` bash
celian  ~  nc challengecybersec.fr 6660
Entrez la reponse ( Enter reply ) : 
 > now
 > Mauvaise reponse !
```

Then we were pretty sure we need to type actual time in the prompt. But, in which format ? After différent tries we found that it was in UNIX Epoch time.

``` bash
celian  ~  date "+%s" | nc challengecybersec.fr 6660
 > Entrez la reponse :
 > Bravo ! Voici le flag : DGSESIEE{cb3b3481e492ccc4db7374274d23c659}
```

