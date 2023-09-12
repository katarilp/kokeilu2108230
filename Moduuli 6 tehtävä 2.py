# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random
tahkot= int(input("Nopan tahkot: "))
def tulos():
    return random.randint(1,tahkot)
silmäluku = tulos()
while silmäluku != tahkot:
    print(silmäluku)
    silmäluku = tulos()
print(silmäluku)
