import random
luku = int(random.randint(1,10))
arvaus = int(input("Arvaa luku väliltä 1-10: "))
# tähän voi laittaa print(arvaus) kokeilun ajaksi
while arvaus < luku:
    arvaus = int(input("Arvaa isompi luku: "))
while arvaus > luku:
    arvaus = int(input("Arvaa pienempi luku: "))
# if arvaus == luku : tähän ei tarvita elseä tai ifiä,
# koska seuraava vaihe tulostetaan jokatapauksessa, kun while-oop päättyy
print("Oikein!")


