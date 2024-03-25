import requests

first_name = input("What Your first name? ")
last_name = input("What Your last name? ")
email_to_send = input("What Your email? ")

sheety_post = "https://api.sheety.co/95aabfd8be11a1b64b16e245c64e968f/flightDeals/users"
user_json = {
    "user": {
        "firstName": first_name.capitalize(),
        "lastName": last_name.capitalize(),
        "email": email_to_send,
    }
}

response = requests.post(url=sheety_post, json=user_json)
print(response.text)

