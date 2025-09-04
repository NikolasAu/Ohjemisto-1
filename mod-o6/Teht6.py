import math

def pintaala(x):
    return math.pi * x ** 2



halkaisija = int(input("Anna pitsan 1 halkaisija: "))
halkaisija2 = int(input("Anna pitsan 2 halkaisija: "))
hinta = int(input("Anna pitsan 1 hinta: "))
hinta2 = int(input("Anna pitsan 2 hinta: "))

sade = halkaisija / 2
sade2 = halkaisija2 / 2

neliohinta =  pintaala(sade) / hinta / 100
print(f"{neliohinta}€ per cm^2")

neliohinta2 = pintaala(sade2) / hinta2 / 100
print(f"{neliohinta2}€ per cm^2")

if neliohinta2 > neliohinta:
    print("pitsa 1 on edullisempi")
else:
    print("pitsa 2 on edullisempi")