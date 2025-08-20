luotim = input("Anna luotien määrä: ")
naulam = input("Anna naulojen määrä: ")
leviskam = input("Anna leviskojen määrä: ")

luoti = 13.3 * float(luotim)
naula = 13.3 * 32 * float(naulam)
leviska = 20 * 13.3 * 32 * float(leviskam)

Paino = luoti + naula + leviska
print(f"{Paino}g")