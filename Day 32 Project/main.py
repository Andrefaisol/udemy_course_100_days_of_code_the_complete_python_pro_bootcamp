# Extra Hard Starting Project #
import smtplib
import datetime as dt
import pandas
import random

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_date = now.day
today_month = now.month
for i in data_dict:
    if i["month"] == today_month and i["day"] == today_date:
        print("yes")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
my_email = ""   # change to your email
my_pass = ""    # change to your email password
list_letter = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
random_letter = random.choice(list_letter)

for i in data_dict:
    if i["month"] == today_month and i["day"] == today_date:
        with open(file=f"letter_templates/{random_letter}", mode="r") as file:
            letter = file.read()
            to_send = letter.replace("[NAME]", i["name"])
        with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connect:
            connect.starttls()
            connect.login(user=my_email, password=my_pass)
            connect.sendmail(from_addr=my_email, to_addrs=i["email"],
                             msg=f"Subject:Happy Birthday! {i["name"]}\n\n{to_send}")
