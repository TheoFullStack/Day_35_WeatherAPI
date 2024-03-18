import requests
API_KEY = "3144248a6e8bc6457859430e1d4a8d81"
LAT= 43.651070
LON = -79.347015
OWM_ENDPOINT = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}"

WEATHER_PARAMS= {
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT,params=WEATHER_PARAMS)
response.raise_for_status()

weather_data = response.json()

#print(weather_data["list"][0]['weather'][0]['id'])
"""print(len(weather_data["list"]))"""


weather_ids = []
for item in weather_data["list"]:
    weather_id = item['weather'][0]['id']
    weather_ids.append(weather_id)
print(weather_ids)


for item in weather_data['list']:
    weather_condition = item['weather'][0]['description']
    pass

weather_id_cond = {
    "id": [item['weather'][0]['id'] for item in weather_data["list"]],
    "condition": [item['weather'][0]['description'] for item in weather_data["list"]]
}


count = 0
for i in range(len(weather_id_cond["id"])):
    count +=1
    if weather_id_cond["id"][i] > 700:
        print(f'This is day {count}, please bring an umbrella. It will be {weather_id_cond["condition"][i]} today.')

