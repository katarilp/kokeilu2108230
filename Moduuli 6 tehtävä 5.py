# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on
# karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
# ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
def karsinta(luvut):
    parilliset = []
    lista = luvut.copy()
    for i in lista:
        if i % 2 == 0:
            parilliset.append(i)
    return parilliset

luvut = [23, 2, 93, 14, 8, 97, 11, 3, 7, 66, 31, 5]
parilliset_lista = karsinta(luvut)
print("Listan kaikki luvut: ")
print(luvut)
print("Listan parilliset luvut:")
print(parilliset_lista)




