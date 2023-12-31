'''Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman
tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä
lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa
sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä
saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
(ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
Löydät koodeja helposti selaimen avulla.)'''

kentät = {}

def kysely(vastaus):
    if vastaus == "haku":
        koodi = input("Anna hakemasi lentoaseman ICAO-koodi: ")
        print(kentät[koodi])

    if vastaus == "uusi":
        koodi = input("Anna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        kentät[koodi] = nimi
    return kentät

vastaus = input("Haluatko syöttää uuden lentoaseman(uusi),\n"
                "hakea jo syötetyn lentoaseman tiedot(haku)\n"
                "vai lopettaa(lopetus)?: ")
vastaus.lower()
while vastaus != "lopetus":
    kysely(vastaus)
    vastaus = input("Haluatko syöttää uuden lentoaseman(uusi),\n"
                   "hakea jo syötetyn lentoaseman tiedot(haku)\n"
                   "vai lopettaa(lopetus)?: ")

if vastaus == "lopetus":
    print("Ohjelma päättyi.")
    quit()