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