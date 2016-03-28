Draft: Crypto over Post Cards
===

Author: Yuriy Ackermann <ackermann.yuriy@gmail.com>

### Status of this Memo

This memo provides information for the Internet community.  It does not specify an Internet standard of any kind.  Distribution of this memo is unlimited.



### Copyright Notice

Ackermann Yuriy. 2016 CC BY-SA 4.0



### Abstract

This document specifies how two parties can establish and use cryptographically strong communication over post cards. The scheme is designed to be secure, efficient, and easy to use, and as much as it could possibly be, paper implementable.



### 1. Rationale and Scope

Sometimes there is need to have secure communication over the post cards, and common means require either share one-time pad, or have preset, previously discussed, and shared key. If two parties have no easy means of communication, then the key must be either shared over insecure channels, or through secure third party. This document describes solution to such an issue, and it called COPC - Crypto over Post Cards.



### 2. COPC scheme

The COPC scheme build on top of existing DH(Diffie-Hellman) key exchange scheme for key establishment, and Vaginere stream cipher for text encryption. To convert decimal key value into poly-alphabetic key, we will reduce key through polynomial Finite Field.



#### 2.1 

#### 2.2 Decimal block reduction through polynomial Finite Field

During DH we will receive decimal value, that is need to be converted to base 26 alphabet. Previous linear approach shown strong pattern and was dismissed. Finally was decided to use same approach as Rijndael, by using polynomial Finite Fields, to create non-deterministic reduction of decimal block.



#### 2.2.1 Ensuring Correct Input

First step is to make sure that decimal block {0..99} lower and upper digits are not zero, and rather large. 

```
    7 * {LD|UD} + 1.
```

This function will ensure that value of LD and UP are bigger then 0. In current document we will call ECI.



#### 2.2.2 Generating Finite Field

Same as Rijndael, we used polynomial approach to create non-deterministic lookup table.

```
    (ECI(LD)^13 + ECI(UP)^11) % 26
```

Numbers 13 and 11 were chosen for the reason of better statistical spread, as both 13 and 11 are prime. Lastly we have to convert given result to base 26 by applying modulo of 26 to the given result.

The resulting char table.
```
   0    1    2    3    4    5    6    7    8    9 
0  e    f    w    p    g    h    y    b    y    t
1  n    w    f    g    p    y    h    i    r    a
2  k    r    y    n    u    b    i    h    o    v
3  t    i    b    k    d    s    l    i    n    c
4  y    d    k    b    i    n    u    p    c    n
5  h    g    z    m    f    e    x    q    b    u
6  u    b    i    d    k    r    y    f    y    f
7  d    s    l    a    t    i    b    g    x    m
8  i    n    u    r    y    d    k    n    m    x
9  r    q    j    a    t    s    l    m    n    g
```

Using this table we can reduce decimal number 42 to 'u', or 69 to 'l'



#### 2.2.3 Python Source Code

Here is implementation in python.

```python
    #Ensuring Correct Input
    def ECI(n):
        return 7 * n + 1

    #Polyniomialiser of finite field
    def PFF(LD, UD): 
        return ((ECI(LD) ^ 13 + ECI(UD) ^ 11) % 26)

    #Generate Finite Field
    def GFF():
        ff = []

        for LD in range(0,10):
            ff.append([PFF(LD, UD) for UD in range(0, 10)])

        return ff

    #Print FF
    def PrintFF():
        ff = GFF()
        for col in ff:
            print([chr(97 + n) for n in col])
```
