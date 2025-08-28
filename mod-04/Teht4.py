import random
from sys import int_info

luku = random.randint(1,10)
while True:
 arvaus = int(input("Arvaa numero 1-10: "))
 if arvaus < luku:
    print("Liian pieni arvaus")
 elif arvaus > luku:
    print("Liian suuri arvaus")
 elif arvaus == luku:
    print("Oikein")
    var = False