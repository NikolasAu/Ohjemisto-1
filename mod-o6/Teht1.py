
import random

def noppa():
    return random.randint(1,6)

while True:
    luku = noppa()
    if luku == 6:
        break
    else:
        print(luku)
