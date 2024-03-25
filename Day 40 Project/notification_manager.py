import requests
from twilio.rest import Client
import smtplib

TWILIO_SID =                 #YOUR TWILIO ACCOUNT SID
TWILIO_AUTH_TOKEN =          #YOUR TWILIO AUTH TOKEN
TWILIO_VIRTUAL_NUMBER =      #YOUR TWILIO VIRTUAL NUMBER
TWILIO_VERIFIED_NUMBER =     #YOUR TWILIO VERIFIED NUMBER


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        self.email_sender = ""
        self.password = ""


    def send_email(self,emails, message):
        with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connect:
            connect.starttls()
            connect.login(user=self.email_sender, password=self.password)
            connect.sendmail(from_addr=self.email_sender, to_addrs=emails,
                             msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8'))

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
