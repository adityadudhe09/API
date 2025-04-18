import json
import requests
import psycopg2
from datetime import datetime

url = "https://ipinfo.io/json"

response = requests.get(url)

timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
ip_data = response.json()

data = {
    'timestamp': timestamp,
    'ip_data': ip_data
}

conn = psycopg2.connect(
    host="postgres",
    database="iptracker",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS ip_logs (
        id SERIAL PRIMARY KEY,
        timestamp VARCHAR,
        ip VARCHAR,
        country VARCHAR,
        city VARCHAR,
        ISP VARCHAR
    )
""")

cur.execute("""
    INSERT INTO ip_logs (timestamp, ip, country, city, org)
    VALUES (%s, %s, %s, %s, %s)
""", (
    timestamp,
    ip_data.get("ip"),
    ip_data.get("country"),
    ip_data.get("city"),
    ip_data.get("org")
))

conn.commit()
cur.close()
conn.close()

with open('ip.json', 'w') as file:
    json.dump(data, file, indent=4)

