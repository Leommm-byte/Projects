import os
import requests
from twilio.rest import Client

api_key = os.environ.get("API_KEY")

account_sid = os.environ.get("TWI_SID")
auth_token = os.environ.get("TWI_AUTH_TOKEN")

parameters = {
    "lat": 6.5960605,
    "lon": 3.340787,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_weather_data = weather_data["hourly"]
twelve_hours = hourly_weather_data[:12]
will_rain = False


for weather_condition in twelve_hours:
    if int(weather_condition["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remeber to bring an ☔",
        from_="+13159035188",
        to="+2348068925885"
    )

    print(message.status)
