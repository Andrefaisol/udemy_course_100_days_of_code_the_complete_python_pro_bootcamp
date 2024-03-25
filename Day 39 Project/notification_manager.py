import smtplib


class NotificationManager:  # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.email_sender = ""
        self.password = ""
        self.email_receiver = ""

    def send_email(self, city, price, seats):
        with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connect:
            connect.starttls()
            connect.login(user=self.email_sender, password=self.password)
            connect.sendmail(from_addr=self.email_sender, to_addrs=self.email_receiver,
                             msg=f"Flight from Jakarta to {city} with price {price} availability seats: {seats}")
