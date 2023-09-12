# Muuttujien näkyvyys (engl. scope)
def print_city(city): # jos sulkeidiin laittaa muuttujan nimen, voi kutsussa laittaa sulkeiden sisäään sen argumentin
                  # esim. f suluissa stad ja kutsutaan stad("Malmö") funktio suoritetaan Malmönä (käyty 1-osassa eilen)
                  # jos sulkeet tyhjät, tulostuu aina local/global arvo
    #city = "Helsinki"  # lokaali muuttuja(local scope) = nämä muuttujat ovat käytössä vain
    city2 = "Vantaa"   # tässä funktiossa, ei mainissa tai muissa funktioissa
    print(city)        # funktion lokaali muuttuja "ylikirjoittaa"(shadows) globaalin muuttujan
    # returnin voi jättää pois, jos funktiosta ei palauteta mitään
    # jos returnin kirjoittaa "keskelle" funktiota, se toimii breakin tavoin ja loppu funktiosta jää suorittamatta

city = "Espoo" # globaali muuttuja(global scope) = käytössä koko ohjelman laajuisesti (jos saman niminen kuin
print_city("Jokioinen")   # funktiossa, ja funktiossa ei määritetä arvoa, funktio voi lainata tämän arvon(ei oletus))
print(city) #sulut aina kutsuvat funktiota(print on sisäänrakennettu funktio)
print_city("Malmö")

def list_sum(num1, num2, num3):
    return num1 + num2 + num3
# print(sum(numbers)) löytyy myös sis.rakennettuna, mutta toteutetaan nyt itse
print(list_sum(1, 4, 7))
nums = [10, 20, 30, 40]

def summa(nums):
    print("Lasketaan listan alkioiden summa: ")
    print(nums)
    result = 0
    for num in nums:
        result = result + num
    return result
print(summa(nums))

# funktio, joka nollaa kaikki listan alkiot
# lista käyttäytyy eri tavoin kuin muut muuttujat
def list_reset(num): # muuttuujan nimi on eri, mutta voi käsitellä mitä vain annettua
    print("Nollataan listan alkiot: ") # listaa 'num' ei ole itsessään olemassa, pelkkä "ontto muuttuja"
    print(num)
    num = num.copy() #Jos halutaan työstää listaa, ilman että alkuperäinen muuttuu pysyvästi
    for i in range(4):
        num[i] = 0
    return num

# myös pääohjelmassa voi tehdä listasta kopion ja suorittaa funktion sen muuttujalla,
# jos ei aina haluta säilyttää alk.per. listaa muuttumattomana
nums2 = [100, 200, 300, 400]
print(list_reset(nums2))
print(nums)
nums100 = [-10, -20, -30, -40]
print(summa(nums100))
print(list_reset(nums100))
print(nums100)


print("Tuple eli monikko eroaa listasta. Sen sältöä ei voi muuttaa.")
# vaihtuvat mittaiset argumenttijonot
def numbers_to_tuple(*nums): # * = ennalta määrittelemätön määrä arvoja
    for num in nums:
        print(num)
    return nums # ei tuota listaa, vaan monikon(TUPLE) erilaiset sulkeet tuntomerkkinä
print(numbers_to_tuple(2,3,57,8,7))
# Tuple vie vähemmän muistia, kuin lista muuttumattomuutensa takia.
# Kannattaa käyttäää varmoissa asioissa, esim viikonpäivät.
tuple1 = (10, 20, 40, 50)
print(tuple1[2])

print("ILTAPÄIVÄN OSUUS: MONIKKO, JOUKKO JA SANAKIRJA; MODUULI 7")
# monikon sisään voi tallettaa toisia monikkoja, merkkijonoja tms.
oma_lista = [1, 2, 3, 4, 5, 6]
print(oma_lista)
oma_monikko = (1, 2,( 3, 4), 5, 6)
print(oma_monikko)
oma_string = "123456"
print(oma_string)

# muokataan
oma_lista[0] = 0        # lista sis. voi muokata (mutable)
print(oma_lista)        # str ja tuple ei voi muokata (immutable)

viikonpäivät = ("ma", "ti", "ke", "to", "pe", "la", "su")
järjestysnumero = int(input("anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print(f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")

#JOUKKO {SET}
# set.add, set.remove
# sama alkio voi esiintyä joukossa vain kerran, tuplat haihtuu
pelit_set = {"monopoli", "shakki", "cluedo"} # järjestäytymätön tietorakenne, printtautuu randomjärjestyksessä
print(pelit_set)
pelit_set.add("uno")
print(pelit_set)

# SANAKIRJA (dictionary) (avain-arvo parit(key-value)) (item = tietue)
oppilaat = {"Aabel": 100, "Bob": 22, "Charlotta": 30, "Daniel": 45, "Elsi": 52}
#printataan koko sanakirjasta avaimet
for i in oppilaat:
    print(i)
#printataan arvot:
for i in oppilaat:
    print(oppilaat[i])

print(oppilaat.items())
print(oppilaat.keys())
print(oppilaat.values())

print(oppilaat["Daniel"]) # hakutoiminto
oppilaat["Felix"] = 61 # uuden lisääminen
print(oppilaat.items())

# arvon muokkaaminen
oppilaat["Aabel"] = 101
print(oppilaat.items())

nimi = input("Anna nimi: ")
if nimi in oppilaat:
    print (f"Henkilön {nimi} ikä on {oppilaat[nimi]}.")

# poistaminen
del oppilaat["Aabel"]
print(oppilaat.items())
# jos halutaan tietoja talteen muuttujaan ennen poistoa
bob = oppilaat.pop("Bob")
print(f"Bob poistettiin sanakirjasta, mutta ikä jäi talteen: {bob}!")
# jos Bob vaihtoi nimeä, tehdään hänelle uusi
oppilaat["Pekka"] = bob
print(oppilaat.items())