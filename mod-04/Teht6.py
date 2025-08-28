import random
import math

maara = int(input("Kuinka monta pistettä arvotaan: "))
kerta = 0
piste = 0

while maara >= kerta:
    kerta = kerta + 1
    x = random.randint(-1,1)
    y = random.randint(-1,1)
    epa = x ** 2 + y ** 2 < 1
    if epa == True:
        piste = piste + 1
print(piste)

pi = 4 * piste / maara
print(pi)