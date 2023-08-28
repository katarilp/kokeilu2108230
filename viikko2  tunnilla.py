print ("Huomenta!")
import math

luku = 3.5
print(math.floor(luku))
print(math.ceil(luku))
print(round(luku))
print(int(luku))

rahat = float(input("Anna rahamäärä: "))
#ehtolause
if rahat >= 5:
    #lohko
    print("Osta latte, ole hyvä.")
if rahat < 5:
    print("Mene kotiisi.")

#
A = True
B = False
#
print(4<69)

lauta = int(input("Anna laudan pituus: "))
if 300 > lauta >= 200 :
    print("Maalaa lauta punaiseksi.")
else :
    print("Kokeile toista lautaa.")


num = int(input("Anna numero: "))
if num < 0 :
    print("Numero on negatiivinen.")
if num == 0 :
    print("Numerosi on nolla.")
if num > 0 :
    print("Numerosi on positiivinen.")