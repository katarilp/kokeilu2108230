luokka = input("Anna hyttiluokka: ")
luokka1 = (luokka.upper())
if luokka1 == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka1 == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka1 == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
elif luokka1 == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
else :
    print("Virheellinen hyttiluokka.")