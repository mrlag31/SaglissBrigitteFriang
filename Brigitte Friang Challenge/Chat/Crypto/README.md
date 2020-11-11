# Crypto

Antoine Rossignol gives us information about another agent, Ève Descartes, who worked on reversing a cryptographic system placed on a card. Before becoming silent, the last agent gave three files. An encrypted archive containing a secret message ([archive_chiffee](./archive_chiffee)), a password protected pdf containing the key needed to decrypt the archive ([layout.pdf](./layout.pdf)), and a pdf of an emailed report containg infomation about the mission ([compte_rendu_eve.pdf](./compte_rendu_eve.png)). It's our goal to uncipher the message by finding a way to contact Ève.

Our first assumption was to contact her via e-mail using the one indicated in her report. Her response was to directly call her phone. Ringing it instantly deliver short and long pulses. These pulses can be translated into morse code spelling the word `resistance`.

Opening [layout.pdf](./layout.pdf) with the password gives us an image with a binary code of 16x16 represented under. *1 represents a cut connection*
```
     Binary       |  Hex  | ASCII
                  |       | 
01000001 01000101 | 41 45 |  A E
01010011 00100000 | 53 20 |  S .
00110010 00110101 | 32 35 |  2 5
00110110 00100000 | 36 20 |  6 .
01000101 01000011 | 45 43 |  E C
01000010 00100000 | 42 20 |  B .
00100000 00100000 | 20 20 |  . .
00100000 00100000 | 20 20 |  . .
00100000 00100000 | 20 20 |  . .
00100000 00100000 | 20 20 |  . .
00100000 00100000 | 20 20 |  . .
00100000 00100000 | 20 20 |  . .
00100000 00100000 | 20 20 |  . .
00100000 00100000 | 20 20 |  . .
00100000 00100000 | 20 20 |  . .
00100000 00100000 | 20 20 |  . .
```
`AES 256 ECB` is a well known encryption algorithm that uses a key of 256 bits, like the one above. Sadly, we did not continue this part because we decided to focus ourselves on other challenges.

*__Note__: [compte_rendu_eve.pdf](./compte_rendu_eve.png) is an image instead of a pdf to hide a phone number because it might be a legitimate phone number.*