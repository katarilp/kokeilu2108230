# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.
import random
nopat = int(input("Kerro noppien lukumäärä: "))
i = 0
heitto = []
for i in range(nopat):
    heitto.append(random.randint(1,7))
    i += 1
summa = sum(heitto)
print(f"Noppien silmälukujen summa on {summa}.")