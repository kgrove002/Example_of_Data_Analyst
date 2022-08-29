import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = "87"
HEIGHT_CM = "183"
AGE = "33"

NUTRITIONIX_KEY = "f0f70adce5051ac7eee9625c0bf178b3"
# NUTRITIONIX_ID = os.environ["nutritionix_id"]
# print(os.environ["nutritionix_id"])
NUTRITIONIX_ID = "d7be8e9d"

SHEETY_ENDPOINT = "https://api.sheety.co/53a31d818d878e1b1edfcd3d61b3aaa9/myWorkouts/sheet1"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise = input("Tell me which exercise you did: ")
duration = input("How long did you do the exercise?")
exercise_text = exercise + duration

now = datetime.now()
current_time = now.strftime("%H:%M")
current_day = now.strftime("%m/%d/%Y")

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutrition_headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY,
    "Content-Type": "application/json"
}

workout_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=nutrition_headers)
workout_result = workout_response.json()

print(workout_result)

basic = ('bqcritken', 'Kmgermsky-07')

for exercise in workout_result["exercises"]:

    sheet_info = {
        "sheet1": {
            "date": current_day,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": duration,
            "calories": exercise["nf_calories"],
        }
    }

    sheet_request = requests.post(url=SHEETY_ENDPOINT, json=sheet_info, auth=basic)
    print(sheet_request.text)
