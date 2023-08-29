#Kuha on alamittainen, jos se on alle 37 cm
mitta = int(input("Anna kuhan pituus: "))
if  mitta >= 37:
    print ("Onnittelut pyyntimittaisesta kuhasta!")
elif mitta < 37:
    print("Kuha on alamittainen. Laske se takaisin järveen.")
    ero = str(37 - mitta)
    print("Pienin pyyntimitta on 37cm. Siihen on matkaa " + ero + "cm.")