import os
import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 150
AGE = 22

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

APP_ID = os.environ["Nutitionix_ID"]
APP_KEY = os.environ["Nutritionix_KEY"]

sheety_url = "https://api.sheety.co/fb09aa1b7ec09c49e471bf28fadae6a2/myWorkouts/workouts"

SHEETY_API_KEY = os.environ["Sheety_API_KEY"]

sheety_header = {
    "Authorization": SHEETY_API_KEY
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

nutritionix_params = {
    "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutritionix_response = requests.post(url=nutritionix_url, json=nutritionix_params, headers=headers)
exercise_data = nutritionix_response.json()

today = datetime.now()

exercise_detail = exercise_data["exercises"]

body = {}
for exercise in exercise_detail:
    exercise_sheet = {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise["name"].title(),
        "duration": round(exercise["duration_min"]),
        "calories": round(exercise["nf_calories"])
    }

    body["workout"] = exercise_sheet
    sheety_response = requests.post(url=sheety_url, json=body, headers=sheety_header)

print("Added Successfully!!")
