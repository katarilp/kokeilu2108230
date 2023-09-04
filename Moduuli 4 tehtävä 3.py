#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku1 = input("Syötä luku tai paina enteriä lopettamisen merkiksi: ")

min = max = luku1
if min == "" or max == "":
    print("Et syöttänyt yhtään lukua.")
    quit()
while luku1 != "":
    luku1 = float(luku1)
    min = float(min)
    max = float(max)
    if luku1 < min:
        min = luku1
    if luku1 > max:
        max = luku1
    luku1 = input("Anna seuraava luku: ")
else:
    print(f'''{min} oli luvuista pienin ja {max} suurin.'''