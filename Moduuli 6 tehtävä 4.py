# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.
def summa(luvut):
    print("Lasketaan listan luvut yhteen: ")
    tulos = 0
    for i in luvut:
        tulos = tulos + i
    return tulos
luvut = [10, 20, 30, 40, 50]
yhteenlaskettu = summa(luvut)

print(yhteenlaskettu)