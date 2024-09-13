import smtplib
import random
import datetime as dt

# Constants
MY_EMAIL = "demahomali01@gmail.com"
RECEIVER = "demahomali02@outlook.com"
MY_PASSWORD = "sunb qasq lchz bhii"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quoteOfTheWeek = random.choice(all_quotes)
    print(quoteOfTheWeek)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"subject:Quote of the Week\n\n{quoteOfTheWeek}"
        )
