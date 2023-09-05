#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
#(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
#Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
#käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

stad = []
i = 0
for i in range(5):
    stad.append(input("Syötä kaupungin nimi: "))
    i += 1
print("Syöttämäsi kaupungit:")
for i in range(5):
    print(f"{stad[i]}")



