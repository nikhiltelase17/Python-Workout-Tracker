import requests
from datetime import datetime


track_api_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
app_id = "6cf4665b"
api_key = "130d7d78b88a8e88d77d5b85ffc5cb3b"
sheet_url = "https://api.sheety.co/06611c666efcc4e05beb6ca9c244f4fa/copyOfMyWorkouts/workouts"
sheet_header = {"Authorization": "Basic bmlraGlsdGVsYXNlOnJhbSByYW0="}
exercise_text = input("Tell me which exercises you did: ")

# --------- GETTING DATA FROM QUERY HELP OF TRACK-API.NUTRITIONIX.COM-------
headers = {"Content-Type": "application/json",
           "x-app-id": app_id,
           "x-app-key": api_key,
           }
body = {"query": exercise_text,
        "weight_kg": 50,
        "height_cm": 169,
        "age": 20,
        }

response = requests.post(url=track_api_url, json=body, headers=headers)
print(response)
workout_data = response.json()["exercises"]

for data in workout_data:
    exercise = data["name"]
    duration = data["duration_min"]
    calories = data["nf_calories"]
    today = datetime.now()
    #  saving data into google sheet
    sheet_body = {"workout": {"date": today.strftime("%d/%m/%Y"),
                              "time": today.strftime("%I:%M:%p"),
                              "exercise": data["name"],
                              "duration": str(data["duration_min"]),
                              "calories": data["nf_calories"],
                              }}

    response = requests.post(url=sheet_url, json=sheet_body, headers=sheet_header)
    print(response)
    print(response.text)
    response.raise_for_status()