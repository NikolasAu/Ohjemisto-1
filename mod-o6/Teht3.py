

def maara(gal):
    return gal * 3.875

while True:
    syote = int(input("Anna galloonamäärä: "))
    if syote < 0:
        break
    litra = maara(syote)
    print(f"{litra} litraa")