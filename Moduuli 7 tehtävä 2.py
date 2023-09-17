# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen
# mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet
# yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
# Käytä joukkotietorakennetta nimien tallentamiseen.

nimet_set = set()

nimi = input("Anna nimi tai paina enteriä lopettaaksesi: ")
def nimikone(nimi):
    if nimi not in nimet_set:
        nimet_set.add(nimi)
        print("Kiitos!")
        return nimet_set
    elif nimi in nimet_set:
        print("Aiemmin syötetty nimi.")
        return

while nimi != "":
    nimikone(nimi)
    nimi = input("Anna uusi nimi tai paina enteriä lopettaaksesi: ")

if nimi == "":
    print(nimet_set)
