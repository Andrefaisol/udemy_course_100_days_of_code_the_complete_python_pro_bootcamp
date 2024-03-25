import requests
import datetime as dt

shiety_get = "https://api.sheety.co/xxxxxxxxxxxxxxx/copyOfMyWorkouts/workouts"
shiety_endpoint_post = "https://api.sheety.co/xxxxxxxxxxxxxxxxxxxx/test1/sheet1"
domain_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
app_id = "xxxxxxxxxxxxxxxxxxxx"
app_key = "xxxxxxxxxxxxxxxxxxxxxxx"
header = {
    "x-app-id": app_id,
    "x-app-key": app_key,
}
GENDER = "male"
WEIGHT_KG = 76
HEIGHT_CM = 173
AGE = 29
nutr_param = {
    "query": input("what you do?"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}
workout_response = requests.post(url=domain_endpoint, headers=header, json=nutr_param)
workout_response.raise_for_status()
workout_json = workout_response.json()
calories = workout_json["exercises"][0]["nf_calories"]
activity = workout_json["exercises"][0]["name"].title()
duration = workout_json["exercises"][0]["duration_min"]
today = dt.datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_hour = today.strftime("%X")

json_to_upload = {
    "sheet1": {
        "date": today_date,
        "time": today_hour,
        "exercise": activity,
        "duration": duration,
        "calories": calories,
    }
}

to_sheet_res = requests.post(shiety_endpoint_post, json=json_to_upload)
print(to_sheet_res.text)
