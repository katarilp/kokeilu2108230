luo = 13.3
nau = 32 * 13.3
lei = 20 * 32 * 13.3
num1 = float(input("Anna paino leivisköinä. "))
num2 = float(input("Anna paino nauloina. "))
num3 = float(input("Anna paino luoteina. "))
num4 = num1 * lei
num5 = num2 * nau
num6 = num3 * 13.3
mas = num4 + num5 + num6
kil = str(mas // 1000)
gra = mas % 1000
gr = str(round(gra,2))
print("Paino on moderneilla yksiköillä " +kil+ " kilogrammaa ja " +gr+ " grammaa.")

#tehtävä 6




