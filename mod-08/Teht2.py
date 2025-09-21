import mysql.connector

def hae_koodilla(icao):
    sql = f"SELECT type, count(*) FROM airport WHERE iso_counrty = %s GROUP BY type"

    kursori = yhteys.cursor()
    kursori.execute(sql, (icao))
    tulos = kursori.fetchall()

    if tulos:
        print("Lentoaseman tyyppija niiden lkm valitsemassasi maassa: ")
        for rivi in tulos:
            print(f"Lentokentän tyyppi: {rivi[0]}, niiden lukumäärä: {rivi[1]}")
        else:
            print("Lentoasemaa ei löytynyt")