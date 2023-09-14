# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def pinta(r, hinta):
        ala = math.pi * r ** 2
        alahinta = hinta / ala
        return alahinta

halk1 = float(input("Kerro ensimmäisen pizzan halkaisina senttimetreinä: "))
hinta1 = float(input("Kerro ensimmäisen pizzan hinta euroina: "))
r = halk1 / 2
hinta = hinta1
pinta(r, hinta)
alahinta1 = pinta(r, hinta)
#print(alahinta1)

halk2 = float(input("Kerro toisen pizzan halkaisina senttimetreinä: "))
hinta2 = float(input("Kerro toisen pizzan hinta euroina: "))
r = halk2 / 2
hinta = hinta2
pinta(r, hinta)
alahinta2 = pinta(r, hinta)
#print(alahinta2)


if alahinta1 > alahinta2:
        print("Toinen pizza antaa paremman vastineen rahalle.")
if alahinta1 < alahinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
if alahinta1 == alahinta2:
        print("Pizzat ovat suhteessa samanhintaiset.")