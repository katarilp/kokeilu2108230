sex = input("Kerro biologinen sukupuolesi: ")
sex1 = (sex.lower())
hg = int(input("Kerro hemoglobiiniarvosi: "))
if sex1 == "mies":
    if hg < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 134 <= hg <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    elif hg > 195:
        print("Hemoglobiiniarvosi on korkea.")
elif sex1 == "nainen":
    if hg < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 117 <= hg <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    elif hg > 175:
        print("Hemoglobiiniarvosi on korkea.")