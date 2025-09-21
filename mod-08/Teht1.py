import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database = "flight_game",
    user="nikolaau",
    passwd= "12345",
    autocommit=True
)

def haelentokentta(koodi):
    sql = f"SELECT name, municipality FROM airport WHERE ident=%s"
    try:
        cursor = yhteys.cursor()
        cursor.execute(sql, (koodi,))
        result = cursor.fetchall()
        if result:
            for rivi in result:
                print(f"Lentokentän nimi: {rivi[0]} ja sijaintikunta: {rivi[1]}")
        else:
            print("Lentokenttää ei löytynyt.")
            cursor.close()
    except mysql.connector.Error as err:
        print(f"Virhe kyselyssä: {err}")




icao_koodi = input("Anna ICAO-Koodi: ")
haelentokentta(icao_koodi)