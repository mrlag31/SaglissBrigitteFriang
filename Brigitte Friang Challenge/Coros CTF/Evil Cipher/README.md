# Evil Cipher

## Description
Evil Country a développé et implémenté sur FPGA son propre algorithme de chiffrement par blocs de 45 bits avec une clé de 64 bits. cipher.txt est un message chiffré avec la clé key=0x4447534553494545. Un agent a réussi à récupérer
- le code VHDL de l'algorithme (evil_cipher.vhd)
- la fin du package VHDL utilisé (extrait_galois_field.vhd)
- le schéma de la fonction permutation15 (permutation15.jpg)
- le schéma du composant key_expansion (key_expansion.jpg)

Un exemple de texte chiffré se trouve dans le fichier evil_example.txt

Déchiffrez le message.

## Reversing VHDL
The first thing is to understand what VHDL is. [VHDL](https://en.wikipedia.org/wiki/VHDL) is a description language for integrated circuits. That means that the described program is translated into a set of connections and logic gates. We will analyze [evil_cipher.vhd](./evil_cipher.vhd).

```vhdl
entity evil_cipher is
  port (
    clk    : in  std_logic;                     -- 1 bit
    resetn : in  std_logic;                     -- 1 bit
    start  : in  std_logic;                     -- 1 bit
    key    : in  std_logic_vector(63 downto 0); -- 64 bits
    din    : in  std_logic_vector(44 downto 0); -- 45 bits
    dout   : out std_logic_vector(44 downto 0); -- 45 bits
    ready  : out std_logic                      -- 1 bit
  );
end entity;
```
These are the connectors outside of the program. In short, these are its inputs (`clk`, `resetn`, `start`, `key`, `din`) and outputs (`dout` , `ready`). Next we have the actual 'program'.

```vhdl
architecture rtl of evil_cipher is
  type state is (idle, cipher);
  signal current_state : state;                       -- Either 'idle' or 'cipher'
  signal next_state    : state;                       -- Either 'idle' or 'cipher'
  signal reg_data      : std_logic_vector(din'range); -- 45 bits
  signal rkey          : std_logic_vector(din'range); -- 45 bits
  signal ctr           : natural range 0 to 5;        -- Counter from 0 to 5
  signal load          : std_logic;                   -- 1 bit
  signal busy          : std_logic;                   -- 1 bit
  
begin
...
end architecture;
```
There are called 'signals' and can be treated as internal variables. On the card, the user cannot directly measure their values. We then have two processes (which are human-readable programs) and a physical connection to some kind of circuit (explained later). In short, the bulk of the algorithm are in those blocks of code:
```vhdl
-- Called on every rising edge of the clock
-- state register
current_state <= next_state;

-- counter
if busy = '0' or ctr=5 then 
  ctr <= 0;
else
  ctr <= ctr+1;
end if;

-- data register
if busy = '1' then 
  if ctr = 0 then
    reg_data <= rkey xor reg_data;
  else 
    reg_data <= round(reg_data,rkey);
  end if;
elsif load = '1' then 
  reg_data <= din;
end if;

---------------

-- Called on every modification of ctr or current_state
case current_state is
  when idle =>
    if start = '1' then 
      next_state <= cipher;  
    else
      next_state <= idle;  
    end if;
    busy <= '0';
    load <= start;
  when cipher =>
    if ctr < 5 then 
      next_state <= cipher;  
    else
      next_state <= idle;  
    end if;
    busy <= '1';
    load <= '0';        
end case;
```

This is how we understood it:
1. You enter `key` and `din` that are repectively 64 and 45 bits.
2. You press `start` and the card starts to cipher `din` by loading `din` in `reg_data`
3. `reg_data` is then modified using the `round` function in `galois_field.vhd`, taking a special key `rkey` and `reg_data`. This is done five time.
4. `reg_data` is then xored with `rkey`.
5. Finally, `reg_data` is outputted on `dout` and `ready` is set to high.

`rkey` is modified on each clock pulse using the special circuit.

The processes in [extrait_galois_field.vhd](./extrait_galois_field.vhd) are easy to understand, there is no real vhdl shenanigans here.

## Reversing circuits

The first one we will look out is [permutation15.jpg](./permutation15.jpg). It simply permutes the order of 15 bits.

The second one is [key_expansion.jpg](./key_expansion.jpg). It is more complicated but one can easily find its purpose. It is mostly made up of muxes and D-flipflops. On clock pulse, when `load` is high, this circuit loads `key` into the D-flipflops which is a register named `reg`. On clock pulse, when `load` is low, the `reg` is looped once on the right, with some added xors on bit 9, 34 and 61. `rkey` is then the 45 first bits of `reg`. This is simply a shift register with some xors to salt the result.

## Galois Fields

Galois fields are a part of [finite fields](https://en.wikipedia.org/wiki/Finite_field). The particular case of Galois fields is the fact that they are fields, which means that there is multiplication, division, addition and subtractions. In our case, we have the field `GF(32)`, which corresponds to a field with 32 or 2^5 elements and is the field corresponding to the set of 5 bits number. Addition and substraction are the same and are behaving like XOR. Multiplication is more subtle. First, every member of a Galois field can be written as a polynomial: `11011` can be written `x^4 + x^3 + x + 1`. Multiplication is done using these polynomials and then reduced to a polynomial of the right size using polynomial modulo and a reducer (`x^5 + x^2 + 1` or `100101`). For example, squaring `11011` yields `101000101` before reduction and `00010` after. This means that `11011*11011 = 00010`.

## Result

We sadly didn't continued mostly due to a lack of time because we tackled this challenge the last day.