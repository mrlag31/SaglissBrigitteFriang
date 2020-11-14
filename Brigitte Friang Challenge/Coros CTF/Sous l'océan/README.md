# Sous l'océan

## Context

> Nous pensons avoir retrouvé la trace d'Eve Descartes. Nous avons reçu un fichier anonyme provenant d'un smartphone Android (probablement celui  de son ravisseur). Retrouvez des informations dans son historique de  position.

We found Eve Descartes' traces. We recieved an anonymous file that comes from an Android Smartphone. Retrieve some data in his position history.

##  Dumpfile

The dumpfile was a memory dump from an android device, inside it, we found out GPS coordinates, we extrated it, cleaned the unneccessary things.

*example of unprocessed GPS dump :* ( see the GPS_dump.txt to see the complete file )

```
Custom Location 1
		gps: Location[gps -47,1462046	30,9018186 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,1963297	30,9012294 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,1970164	30,8641039 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,1438013	30,8652827 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,1448313	30,9642508 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
	Custom Location 2
		gps: Location[gps -47,0820032	30,8641039 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,1300684	30,8643986 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,1304118	30,9006402 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,0789133	30,9003456 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,0847498	30,8131067 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,1307551	30,8148758 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,1304118	30,8340395 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,1084391	30,8319759 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
	Custom Location 3
		gps: Location[gps -47,0631205	30,8649880 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,0322214	30,9015240 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,0047556	30,8608621 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
		gps: Location[gps -47,0411478	30,8632198 hAcc=20 et=??? alt=0.0 vel=0.0 bear=0.0 vAcc=??? sAcc=??? bAcc=??? {Bundle[{satellites=0, maxCn0=0, meanCn0=0}]}]
```

