import random
luku = int(random.randint(1,10))
arvaus = int(input("Arvaa luku väliltä 1-10: "))
while arvaus < luku:
    arvaus = int(input("Arvaa isompi luku: "))
while arvaus > luku:
    arvaus = int(input("Arvaa pienempi luku: "))
if arvaus == luku :
    print("Oikein!")


