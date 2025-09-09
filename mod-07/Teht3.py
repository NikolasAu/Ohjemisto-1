from Tools.scripts.generate_global_objects import Printer

koodit = {"Helsinki-Vantaa":"EFHK",
           "Rovaniemi":"EFRO",
           "Kuopio":"EFKU",
         "Jyväskylä":"EFJY",
         "Tampere-Pirkkala":"EFTP"}

while True:
    syote = input("Haluatko syöttää lentoaseman tiedot. Kyllä vai ei: ")
    if syote == "ei":
        break
    elif syote == "kyllä":
        print("Jos haluat vielä lopettaa ohjelman. Kirjoita lopeta")
        koodi = input("Syötä lentoaseman ICAO-koodi: ")
        if koodi == "lopeta":
            break
        else:
            if koodi in koodit:
                print(f"Lentokenttä: {koodi}, lentokentän koodi: {koodit[koodi]}")
    else:
        print("Virheellinen syote")
