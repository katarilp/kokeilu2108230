# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random
print("Nopan silmäluvut:")
def tulos():
    heitto = random.randint(1,6)
    return heitto
silmäluku = tulos()
while silmäluku != 6:
    print(silmäluku)
    silmäluku = tulos()
print(silmäluku)


