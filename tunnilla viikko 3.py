# lista ja for 5.9.2023

names = ["Väinö", "Veera", "Verneri", "Vekkuli", "Verla", "Venla", "Vieno"]
# listassa jokaisella alkiolla on indeksinumero alkaen nollasta
ages = [5, 6.6, 8, 3, 88, 7, 9]
#print(f"{names[2]}, ikä {ages[2]} vuotta")
print(f"voidaan tulla toisesta päästä miinuksella {names[-2]}")
print(f"alueena printattu, jolloin vika jää pois {names[0:3]}")
print(f"aloitetaan jostain ja jätetään yläraja auki: tulostaa kaikki loppuun asti{names[4:]}")

iterator = 0
while iterator < 6: #tähän voisi myös laittaa iterator < len(names), niin tulee kaikki
                    # huom: ei saa olla =< tai pitäis merkata len(names) -1
    print(f"{names[iterator]}, ikä {ages[iterator]} vuotta")
    iterator += 1
'''
# listan pituus saadaan, kun otetaan len()-funktio ja laitetaan listan nimi sen sisään
lenght = len(names)
print(lenght)
names.append("uusi nimi listan loppuun")
print(names)
names.remove("Verla")
print(names)
names.insert(0,"Vauva")
print(names)
names.extend(ages)
print(names)
names2 = names[0:3]
print(names2)
print(names.index("Veera"))
'''
'''
# Löytyykö arvo listalta?
hakusana = input("Kuka olet? ")
if hakusana in names:
    print(f"Nimesi {hakusana} löytyy listalta.")
else:
    print("Sinä et ole kutsuvieriden listalla")
'''
'''
# nimen lisääminen
newname = input("Kerro nimesi: ")
names.append(newname)
print(names)
'''
# FOR-silmukka

for name in names: #tulostaa kaikki
    print(f"Nimi: {name}")

print("------")
for i in range(3): # 0,1,2, i = iterator
    print(f"nimi: {names[i]}")

print("------")
for i in range(len(names)):
    print(f"nimi: {names[i]}, ikä: {ages[i]}")

print(".......")
for i in range(0, 16, 2): #ekat näyttää vlin ja kolmas millä väleillä valitaan luvut
    # voidaan menää myös luvuissa alaspäin (999, 0, -3)
    print(i)

