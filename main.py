import requests
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC05d04e361c0682865032602ba14f30ca"
auth_token = "d7ced1f6adf0c60d525cc45346127401"
client = Client(account_sid, auth_token)


















#API_KEY = "3144248a6e8bc6457859430e1d4a8d81"
API_KEY = os.environ.get("OWM_API_KEY1")
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

it_rains = False
count = 0
for i in range(len(weather_id_cond["id"])):
    count +=1
    if weather_id_cond["id"][i] < 700:
        it_rains = True

if it_rains:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today. Bring an umbrella",
        from_='+15315414858',
        to='TARGET PHONE NUMBER'
    )
    print(message.status)

