# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.


number = int(input("Anna kokonaisluku: "))
isPrime = True
for i in range(2, number):
    if number % i == 0:
        isPrime = False
        print(f"Luku {number} ei ole alkuluku.")
        break
if isPrime == True :
    print(f"Numero {number} on alkuluku.")