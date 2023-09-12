# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan
# vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää
# negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def muunnos(num):
    tulos = num * 3.785
    return tulos

num = float(input("Anna bensiinin määrä nestegallonoina: "))
while num >= 0:
    litrat = muunnos(num)
    print("Bensiinin määrä litroina:")
    print(litrat)
    num = float(input("Anna bensiinin määrä nestegallonoina: "))
