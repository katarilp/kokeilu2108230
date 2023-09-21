import mysql.connector
# CREATE USER IF NOT EXISTS 'Kata'@'localhost' IDENTIFIED BY 'password';
# GRANT ALL PRIVILEGES ON `flight_game`.* TO 'Kata'@'localhost';

# muodostetaan yhteys
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='Kata',
         password='password',
         autocommit=True
         )
cursor = connection.cursor()
# cursor.execute("select iso_country, name from country where iso_country = 'FI'")
# result = cursor.fetchone() hakee vain ensimmäisen tulosrivin
# print(result)

cursor.execute("select iso_country, name from country where continent = 'EU'")
# jos selectin sijasta olis update, voisi muuttaa kannan tietoja
# insertillä voisi lisätä esim uusia pelaajia
result = cursor.fetchall()
# print(result) tulisi lista, jossa tupleja
print(cursor.rowcount) # kertoo kuinka monta tulosta on tai montaako riviä muutos/haku koskee
for country in result:
    print(f"Maa: {country[1]}, koodi: {country[0]}")

def get_country_by_iso_code(iso_code):
    cursor = connection.cursor()
    sql = f"select iso_country, name from country where iso_country = '{iso_code}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return result[1]
    else:
        return "No results."


country = get_country_by_iso_code('FI')
print(country)
country = get_country_by_iso_code(input("Syötä maakoodi: "))
print(country)
