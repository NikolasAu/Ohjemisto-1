luvut = []

luku = input("Anna Luku: ")
luvut.append(luku)

while luku != "":
    luku = input("Anna Luku: ")
    luvut.append(luku)

luvut.sort(reverse=True)

for luku in luvut[:5]:
    print(luku)