import math

vuosi = int(input("Anna vuosiluku: "))
vuosi1 = float(vuosi) / 4
vuosi2 = float(vuosi) / 100

if vuosi1.is_integer():
    print("Vuosi on karkausvuosi")
elif vuosi2 / 400 and vuosi2.is_integer():
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")