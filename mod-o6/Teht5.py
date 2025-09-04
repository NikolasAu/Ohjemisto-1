lista2 = []

def list(luvut):
    for i in luvut:
        if i % 2 == 0:
            lista2.append(i)
    return lista2

lista = [2, 6, 4, 7, 8, 9, 10]
print(lista)
print(list(lista2))
