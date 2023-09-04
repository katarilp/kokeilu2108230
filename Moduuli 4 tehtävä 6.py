import random
# x ** 2 + y ** 2 < 1

N = int(input("Syötä pisteiden määrä: "))
n = kierros = y = x = 0
# x ja y arvoja ei välttämättä tarvitse tässä vaiheessa määrittää

while kierros < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
#   print(f"x: {x} ja y: {y}") jos kokeilee pienillä määrällä
    kierros += 1
    if x ** 2 + y ** 2 < 1: #== True:
        n += 1

print(4 * n / N )