# Le discret Napier

## Description

Stockos a encore choisi un code d'accès qui est solution d'une énigme mathématique ! Retrouvez x tel que : 17^x ≡ 183512102249711162422426526694763570228 [207419578609033051199924683129295125643]

## Slow Solution

This is clearly a problem about discrete logarithms. Trying every value of `x` is out of the question. Trying to resolve it, we used a mix of two algorithm: [Pohlig-Hellman](https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm) and [Pollard's rho](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm_for_logarithms). Algorithms were written to be executed with [bdcalc](https://www.di-mgt.com.au/bdcalc.html).

- [Polhig-Hellman.bdscr](./Polhig-Hellman.bdscr) prints the list of `pi` and their coresponding `gi`, `hi`.
- [Pollards-rho.bdscr](./Pollards-rho.bdscr) calculates `x`, solution of `a^x = b [p]` reduced with Polhig-Hellman algorithm.

Sadly, yet again due to a lack of time, we did not finished this challenge.