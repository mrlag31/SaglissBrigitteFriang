# Keypad Sniffer

### Challenge

For this challenge, we know that someone put a sniffer on a keypad. We also have the output file of the sniffer and these 2 pics :

<p align="center">
    <img width=50% src="./keypad_face.jpg" style="float: left" alt="keypad_face">
    <img width=50% src="./keypad_back.jpg" style="float: left" alt="keypad_back">
</p>

The goal of this challenge is to retrieve the code pressedo on the keypad.

### Search

#### How keypad works ?

Before that we never worked with a keypad, after some search we discovered that it's simple and it's just a multiplexing of column and row.

On the side of the microcontroleur, it's not very complex too : 

- Columns are output ( low level at start )
- Rows are input ( high level at start )

Then to detect which key is pressed, the controller scan in loop each column by setting it to high value. If a row is at high value then we know which column and which row and then the key. 

#### Wiring

Now that we know how it works, we need to figure out what each bit in our file is related to.

We have a 4x4 keypad so we are supposed to have 8 usd bits but our file contain 12.

Here are the first lines in the file :

10111110**0**111
10111110**0**111
10111110**0**111
10111110**0**111
10111110**0**111
10111110**0**111
10111110**0**111
10111110**0**111
101111101**0**11
101111101**0**11
101111101**0**11
101111101**0**11
101111101**0**11
101111101**0**11
101111101**0**11
101111101**0**11
1011111011**0**1
1011111011**0**1
1011111011**0**1
1011111011**0**1
1011111011**0**1
1011111011**0**1
1011111011**0**1
10111110111**0**
10111110111**0**
10111110111**0**
10111110111**0**
10111110111**0**
10111110111**0**
10111110111**0**

In bold we can easily see a part that looks like a lot of the scan part. So this 4 bits are useful. We also know can see if we scroll more in the file that bits [0:1] and [7:8] never change.

So, we know that bits [2:6] are inputs and [9:12] are for the scan. Only thing we don't know is the order and if row or columns are used as scan but we will deal with that in the script.

###  Solve

Now we know how the keypad works, let's implement that in a script.
To simplify this part we first removed bits [2:6] and [9:12] from the file.

