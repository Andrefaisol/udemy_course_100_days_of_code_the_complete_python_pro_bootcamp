import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
HEADER = {"Accept-Language": "en-US,en;q=0.9",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0"
          }
my_email = ""
my_pass = ""
email_to_send = ""

response = requests.get(url=URL, headers=HEADER).text
soup = BeautifulSoup(response, "lxml")
price = soup.find("span", class_="a-price-whole")
cleaned = int((price.getText()).replace(".", ""))

min_price = 130
if cleaned < min_price:
    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connect:
        connect.starttls()
        connect.login(user=my_email, password=my_pass)
        connect.sendmail(from_addr=my_email, to_addrs=email_to_send,
                         msg=f"Subject:Your Wishlist get price down!\n\nThe item with url: "
                             f"{URL} get price down less than usd {min_price}")
