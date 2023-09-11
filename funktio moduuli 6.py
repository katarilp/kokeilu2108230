# def = define, funktion nimi, (mahdolliset parametrit)
# funktio pitää määritellä ennen kuin sitä kutsutaan
def tervehdi():
    print("Moi!")
    print("Nyt ollaan funktion sisällä. Ohjelman suoritus siirtyi tänne, ")
    return

# pääohjelma (funktion koodi suoritetaan vain kutsuttaessa)
print("Terve! Tämä on pääohjelma.")
tervehdi()   #kutsutaan funktiota
print("jonka jälkeen palasimme pääohjelmaan.")

# funktioiden sisällä voi olla vaikka mitä toimintoja
# ja funktioden sisälä voidaan kutsua toisia funktioita ehdon täyttyessä

def tervehdi_käyttäjää():
    print("Moi taas :)")
    return # return palauttaa pääohjelmaan paluuarvon (jos sellainen on)

def main():
    tervehdi_käyttäjää()

main()

def tervehdi(kerrat): # kerrat on parametrimuuttuja, johon annettu argumentti hyppää
    for i in range(kerrat):
        print ("Hyvää päivää " + str(i+1) + ". kerran")
    return
'''
kertaa = int(input("Montako kertaa tervehditään?" ))

tervehdi(kertaa) # suluissa on argumentin arvo
print ("Tervehditään lisää.")
tervehdi(2)
'''
# parametrit ja paluuarvo
def printtaa_summa(x, y):  # tämä funktio ei palauta mitään
    print(x + y)
    return

printtaa_summa(5, 8)
printtaa_summa (100, 500)

# paluuarvon palauttava funktio
def summa(x, y):  # funktion sisällä voi myös printata,
    yht = x + y   # mutta paluuarvoa voidaan käyttää pääohjelmassa johonkin
    return yht

tulos = summa(10, 15)
print(tulos)

# funktioiden muita piirteitä
def tietoja(nimi, ikä, harrastus):
    tervehdys = f"Terve {nimi}. Ikäsi on {ikä} ja suosikkiharrastuksesi on {harrastus}."
    return tervehdys

henkilö = tietoja("Ulla", 21, "enduro")
print(henkilö)

# parametrien välittäminen muuttujan avulla, (nimi = arvo)-pari
henkilö2 = tietoja(nimi ="Pekka", ikä = 101, harrastus ="kalastus")

print(henkilö2)

# jos ei tiedä arvoa
def tietoja2(nimi, ikä, harrastus="ohjelmointi"): # on annettu oletusarvo
    tervehdys = f"Terve {nimi}. Ikäsi on {ikä} ja suosikkiharrastuksesi on {harrastus}."
    return tervehdys

henkilö3 = tietoja2("Pekka", 23)
print(henkilö3)