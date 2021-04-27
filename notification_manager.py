from twilio.rest import Client
import smtplib
from flight_data import FlightData
from data_manager import DataManager
import os

TWILIO_SID = os.environ['SID']
TWILIO_AUTH_TOKEN = os.environ['AUTH_TOKEN']
TWILIO_VIRTUAL_NUMBER = os.environ['VIRTUAL_NUMBER']
TWILIO_VERIFIED_NUMBER = os.environ['VERIF_NUMBER']

my_email = os.environ('EMAIL')
my_password = os.environ['EMAIL_PASS']

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, message):
        data = DataManager()
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(from_addr=my_email, to_addrs=data.grab_creds(), msg=f"Subject: Flight Deals \n\n {message}")