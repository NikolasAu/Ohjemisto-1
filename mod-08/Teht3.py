import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database = "flight_game",
    user="nikolaau",
    passwd= "12345",
    autocommit=True
)

icao = input("Anna ensimmäisen kentän ICAO-koodi: ")
sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = "{icao}"'
kursori = yhteys.cursor()
kursori.execute(sql)
kenttaA = kursori.fetchone()

icao = input("Anna toisen kentän ICAO-koodi: ")
sql = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident = "{icao}"'
kursori = yhteys.cursor()
kursori.execute(sql)
kenttaB = kursori.fetchone()

etaisyys = distance.distance(kenttaA, kenttaB).km

print(f"Lentokenttien etäisyys on {etaisyys:.0f} km")