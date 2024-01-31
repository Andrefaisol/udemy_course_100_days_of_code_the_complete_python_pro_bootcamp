import smtplib
import datetime as dt
import random

# insert email
my_email = ""
# insert email password
my_pass = ""

now = dt.datetime.now()
this_year = now.year
this_month = now.month
this_day = now.weekday()
birthday = dt.datetime(year=1994, day=11, month=6)
day_dict = {"sunday": 6, "monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5}

with open(file="quotes.txt", mode="r") as file:
    turn = file.read()
    q_list = turn.split("\n")

ran_quote = random.choice(q_list)
ran_day = random.randint(1, 30)

if this_day == day_dict["wednesday"]:
    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connect:
        connect.starttls()
        connect.login(user=my_email, password=my_pass)
        connect.sendmail(from_addr=my_email, to_addrs="",
                         msg=f"Subject:Motivation Day {ran_day}\n\n{ran_quote}")
