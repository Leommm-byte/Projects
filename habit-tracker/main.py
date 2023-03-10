import requests
from datetime import datetime

USERNAME = "teggyg"
TOKEN = "kshktehi34m934jejoreiut8"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "mins",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

graph_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

graph_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today?: ")
}

response = requests.post(url=graph_pixel_endpoint, json=graph_pixel_config, headers=headers)
print(response.text)

yesterday = datetime(year=2023, month=3, day=5)
pixel_mod_endpoint = f'{graph_pixel_endpoint}/{yesterday.strftime("%Y%m%d")}'

update_pixel_config = {
    "quantity": "75"
}

# response = requests.put(url=pixel_mod_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# response = requests.delete(url=pixel_mod_endpoint, headers=headers)
# print(response.text)
