import random

numerot = []

arpa = int(input("Anna arpakuutioiden määrä: "))

for i in range (arpa):
    numero = random.randint(1,6)
    numerot.append(numero)

numerotsumma =sum(numerot)
print(numerotsumma)