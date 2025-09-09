vuodenajat = (("kevät", (1,2,3)), ("kesä", (4,5,6)), ("syksy", (7,8,9)), ("talvi", (10,11,12)))

syote = int(input("Anna kuukauden numero: "))

kuukausi = vuodenajat[syote-1]
print(kuukausi)