import requests
import mysql.connector

API_KEY = "API"

url = f"https://api.openweathermap.org/data/2.5/weather?q=Helsinki&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(data)

# Tarkista että data on oikein
if "main" not in data:
    print("❌ Virhe API:ssa:", data)
    exit()

#  Ota arvot
temp = data["main"]["temp"]
humidity = data["main"]["humidity"]

# Yhdistä MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="exampleuser",
    password="salasana123",
    database="exampledb"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    temperature FLOAT,
    humidity INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Lisää data
cursor.execute(
    "INSERT INTO weather (temperature, humidity) VALUES (%s, %s)",
    (temp, humidity)
)

conn.commit()

# Sulje yhteys
cursor.close()
conn.close()

print(" Data tallennettu!")
