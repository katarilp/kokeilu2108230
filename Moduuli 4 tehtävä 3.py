#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku1 = input("Syötä luku tai paina enteriä lopettamisen merkiksi: ")
if luku1 == "":
    print("Et syöttänyt yhtään lukua.")
else :
    luku1 = input("Syötä uusi luku tai paina enteriä lopettamisen merkiksi : ")
    if luku1 == "":
        suurin = luku1
        pienin = luku1
        pienin1 = int(pienin) - 1
        suurin1 = int(suurin) + 1
        int(pienin1)
        int(suurin1)
        print("Syöttämistäsi luvuista suurin oli " +str(suurin1)+ " ja pienin " +str(pienin1)+ ".")
        if int(luku1) < int(pienin1):
            luku1 = pienin1
        elif int(luku1) > int(suurin1):
            luku1 = suurin1

