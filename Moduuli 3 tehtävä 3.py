sex = input("Kerro biologinen sukupuolesi: ")
sex = sex.lower()
hg = int(input("Kerro hemoglobiiniarvosi: "))
if sex != "mies" and sex != "nainen":
    print("Virheellinen sukupuoli.")
    quit()
if sex == "mies":
    if hg < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 134 <= hg <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    elif hg > 195:
        print("Hemoglobiiniarvosi on korkea.")
elif sex == "nainen":
    if hg < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 117 <= hg <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    elif hg > 175:
        print("Hemoglobiiniarvosi on korkea.")