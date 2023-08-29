tuuma = float(input("Anna tuumamäärä: "))
while tuuma > 0 and tuuma != 0:
    print(f"Antamasi tuumamäärä on {tuuma * 2.54} cm.")
    tuuma = float(input("Anna tuumamäärä: "))
    if tuuma == 0:
        print("Älä syötä nollaa.")
        tuuma = float(input("Anna tuumamäärä: "))
else :
    print("Annoit negatiivisen tuumamäärän. Ohjelma päättyi.")