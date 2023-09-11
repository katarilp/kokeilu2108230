# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

jono = []
luku = input("Anna luku, tai paina enteriä ohjelman lopettamiseksi: ")
if luku == "":
    print("Et syöttänyt yhtään lukua.")
    quit()
while luku != "":
    jono.append(int(luku))
    jono.sort(reverse=True)
    luku = input("Anna uusi luku tai paina enteriä ohjelman lopettamiseksi: ")

print(f"Viisi suurinta syöttämääsi lukua olivat: {jono[0:5]}")
