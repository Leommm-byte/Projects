import requests
from twilio.rest import Client

api_key = "e0236ac09fbfbbf8b08235f6e1eff0ac"

account_sid = "ACae6761704379db12e2a381a5842375a9"
auth_token = "5b7423397921644dd73cde50a78428ef"

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
