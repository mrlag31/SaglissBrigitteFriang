# Forensic

## Context

> Un agent d'Evil Gouv a réussi à se connecter sur notre plateforme, il faut absolument que l'on retrouve son adresse IP

We are told by the Forensic Service that someone accessed their network, we have to find who did this.

### access.log

We were given an nginx access log file. Inside the log we had to find the right IP address to block it. So by using the search function in the file we blocked the only IP that pointed to "evil" content, such as `evil browser`

```log
188.37.251.216 - - [Nov 05 2020 16:20:43] "GET /img/image.jpg HTTP/1.1" 200 352 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13"
142.98.150.84 - - [Nov 05 2020 16:22:04] "GET /img/team.jpeg HTTP/1.1" 200 33 "-" "Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9b5) Gecko/2008041514 Firefox/3.0b5"
179.97.58.61 - - [Nov 05 2020 16:22:20] "POST /login HTTP/1.1" 200 476 "-" "Evil Browser"
162.73.96.211 - - [Nov 05 2020 16:23:40] "GET /img/logo.ico HTTP/1.1" 200 264 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13"
176.6.24.77 - - [Nov 05 2020 16:25:34] "GET /img/image.jpg HTTP/1.1" 200 49 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.75 Safari/537.1"

```

An extract to show how the document were formatted with the answer inside.

### desert.jpg

The desert.jpg was given by the forensic chief after we gave the right IP address.
This file were an hidden .zip file `opening` it and `extracting` the content gave us 2 files, `part2.img` and `part3.img`

### part2.img & part3.img