import os
import pandas
import random
import datetime as dt
import smtplib, ssl

# 1. Update the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")
new = birthdays.to_dict(orient="records")
PLACEHOLDER = "[NAME]"
LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")

now = dt.datetime.now()
day = now.day
month = now.month

context = ssl.create_default_context()

# 2. Check if today matches a birthday in the birthdays.csv
for position in new:
    if position["month"] == month and position["day"] == day:
        # If true, pick a random letter from letter templates and
        # replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/{random.choice(LETTERS)}", "r") as letter:
            letter_content = letter.read()
            new_letter = letter_content.replace(PLACEHOLDER, position["name"])

            msg = f"Subject:Happy Birthday\n\n{new_letter}"

            # Send the letter generated in previous step to that person's email address.
            with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as connection:
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=position["email"], msg=msg)

