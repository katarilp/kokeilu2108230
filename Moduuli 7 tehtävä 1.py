# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä
# vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat
# merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi
# siten, että joulukuu on ensimmäinen talvikuukausi.
#
talvi = (12, 1, 2)
kevät = (3, 4, 5)
kesä = (6, 7, 8)
syksy= (9, 10, 11)

numero = int(input("Anna kuukauden järjestysnumero: "))
if numero in talvi:
    print ("Talvi")
elif numero in kevät:
    print ("Kevät")
elif numero in kesä:
    print ("Kesä")
elif numero in syksy:
    print("Syksy")
else:
    print("Kelvoton numero.")

