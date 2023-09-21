# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja
# sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.


import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='Kata',
         password='password',
         autocommit=True
         )
cursor = connection.cursor()

icao = input("Anna hakemasi lentoaseman ICAO-koodi: ")
icao.upper()

cursor.execute(f"select name, municipality from airport where ident = '{icao}'")
result = cursor.fetchall()
print(result)