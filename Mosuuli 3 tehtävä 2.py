luokka = input("Anna hyttiluokka: ") # tai tähän voisi laittaa .upper() ja myöhemmin kaikissa vain luokka ilman upperia
if luokka.upper() == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka.upper() == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka.upper() == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
elif luokka.upper() == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
else :
    print("Virheellinen hyttiluokka.")