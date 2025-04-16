import json
import requests
from datetime import datetime

url = "https://ipinfo.io/json"

response = requests.get(url)

current_time = datetime.now()
format_time = current_time.strftime("%d-%m-%Y %H:%M:%S")

data = {
    'timestamp': format_time,
    'ip_data': response.json()
}
with open('ip.json', 'w') as file:
    json.dump(data, file, indent=4)