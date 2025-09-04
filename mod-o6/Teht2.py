import random

silma = int(input("Anna silmäluku: "))

def noppa():
    return random.randint(1,silma)

while True:
    luku = noppa()
    print(luku)
    if luku == silma:
        break