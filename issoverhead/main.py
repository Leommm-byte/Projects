import smtplib
import ssl
from datetime import datetime
import requests
import time


MY_LAT = 6.637560
MY_LONG = 3.345870
MY_EMAIL = "trainpythonista@gmail.com"
PASSWORD = "bsqnnazakftzsyqb"
context = ssl.create_default_context()


def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour

    if hour >= sunset or hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_close() and is_night():
        with smtplib.SMTP_SSL("smtp.gmail.com", port=587, context=context) as server:
            server.login(user=MY_EMAIL, password=PASSWORD)
            server.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky"
            )
    else:
        print("Still running")
