# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.
import random
nopat = int(input("Kerro noppien lukumäärä: "))
heitto = []
#summa = 0
for i in range(nopat):
    heitto.append(random.randint(1,6))
#voi summata myös loopin sisällä summa = summa + heitto[i]
summa = sum(heitto)
print(f"Noppien silmälukujen summa on {summa}.")