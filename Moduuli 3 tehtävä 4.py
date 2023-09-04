year = int(input("Anna vuosiluku: "))

# if year % 4 == 0 and year % 400 == 0 or year % 4 == 0 and year % 100 != 0: olisi sama yhdellä rivillä
if year % 100 == 0 and year % 400 == 0:
    print("Antamasi vuosi on karkausvuosi.")
elif year % 4 == 0 and year % 100 != 0:
    print("Antamasi vuosi on karkausvuosi.")
else :
    print("Antamasi vuosi ei ole karkausvuosi.")