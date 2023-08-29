import random
noppa1 = noppa2 = heitot = 0
while noppa1 !=6 or noppa2!=6:
    noppa1 = random.randint(1, 6)
    noppa2 = random.randint(1, 6)
    heitot = heitot + 1
print(f"Tarvittiin {heitot:d} heittoa.")

# whilen täytyy totettaa True, että hypätään while-looppiin.
# voisi olla myös invertoituna while not (nopa1 == 6 and noppa2 == 6)