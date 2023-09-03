tunnus = input("Anna käyttäjätunnus: ")
salis = input("Anna salasana: ")
if tunnus == "python" and salis == "rules":
    print("Tervetuloa!")
else :
    kerrat = 1
    while kerrat < 5:
        tunnus = input("Anna käyttäjätunnus: ")
        salis = input("Anna salasana: ")
        kerrat += 1
    if kerrat == 5:
        print("Pääsy evätty.")
