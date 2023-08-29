#28.8.2023 Ulla

print ("Huomenta!")
import math
luku = 3.5
print(math.floor(luku))
print(math.ceil(luku))
print(round(luku))
print(int(luku))

rahat = int(input("Anna rahamäärä: "))
#ehtolause
if rahat >= 5:
    #lohko
    print("Osta latte, ole hyvä.")
if rahat < 5:
    print("Mene kotiisi.")

A = True
B = False
print(4<69)

lauta = int(input("Anna laudan pituus: "))
if 300 > lauta >= 200 :
    print("Maalaa lauta punaiseksi.")
else :
    print("Kokeile toista lautaa.")

num = int(input("Anna numero: "))
if num < 0:
    print("Numero on negatiivinen.")
if num == 0:
    print("Numerosi on nolla.")
if num > 0:
    print("Numerosi on positiivinen.")

#29.8.2023 Matti
# jos on peräkkäin monta iffiä, kaikki testataan, vaikka eka olisi jo totta JA huomioidaan eri if-haarojen elset.
# Eliffejä ei käydä läpi, jos aikaisempi vaihtoehto on ollut totta.
user_input = input("a vai b? ")
if user_input == "a": #tähän voisi syöttää myös 'if not'
    print("Tee jotain.")
    print("Tähän voi lisätä monta riviä.")
elif user_input == "b":
    print("Käyttäjä valitsi b:n. Ei tehdä mitään.")
else :
    print("Käyttäjä ei syöttänyt annettua vaihtoehtoa. Tehdään jotain yllättävää.")
print("Ohjelman suoritus jatkuu tästä.")

#Loogiset operaattorit: and, or not (joissain kielissä and=&& ja not True = !=)
age = 5
name = "Ville"
print(age < 10 and name == "Ville")
print(age < 10 or name == "Viivi")
print(age < 10 and not name == "Viivi")
print(not True)

#lääke-esimerkki kalvoilta muunneltuna
ikä = int(input("Anna ikä: "))
if 15<=ikä<18: # sama ehto toisin: 15 <= ikä and age > 18
    paino = float(input("Anna paino (kg): "))
    if paino >= 55:
        print("Lääkkeen käyttö on sallittua.")
elif ikä >= 18 :
    print("Lääkkeen käyttö on sallittua.")
else :
    print("Konsultoi lääkäriä.")

#while
kerrat = int(input("Montako kertaa tervehditään: "))
tehdyt = 0
while tehdyt < kerrat:
    print("Hyvää huomenta!")
    tehdyt = tehdyt + 1

komento = input("Anna komento: ")
while komento != "lopeta":
    print("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
print("Toiminnot lopetettu.")

luku = int(input("Kuinka monta kertaa koiran pitää haukkua? "))
haukut = 0
while haukut < luku:
    print("Wuf!")
    haukut = haukut + 1 # voi kirjoittaa myös 'haukut += 1'

taikasana = input("Musti haukkuu. Käske sen olla hiljaa sanomalla 'stop'! ")
while taikasana != "stop":
    haukut = 0
    while haukut < 3:
        print("Wuff!")
        haukut += 1
    taikasana = (input("Musti haukkuu. Käske sen olla hiljaa sanomalla 'stop'! ")