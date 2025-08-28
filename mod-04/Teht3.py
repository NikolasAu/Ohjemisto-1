from operator import truediv
pienin = 0
suurin = 0

luku = input("Anna Luku: ")
pienin = luku
suurin = luku
while True:
    luku2 = input("Anna luku: ")
    if luku2 == "":
        break
    elif luku2 < pienin:
        pienin = luku2
    elif luku2 > suurin:
        suurin = luku2

print(pienin)
print(suurin)