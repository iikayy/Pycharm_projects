import smtplib
import pandas
import datetime as dt
import random

today = dt.datetime.now()
day = today.day
month = today.month

birthday_df = pandas.read_csv("birthdays.csv")
for (index, row) in birthday_df.iterrows():
    if month == row.month and day == row.day:
        name = row["name"]
        letter_template_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(letter_template_path) as letter_file:
            letter = letter_file.read().replace("[NAME]", name)

        my_email = "benblacck@gmail.com"
        password = "nqaonvxsembaeazn"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="benblacck@outlook.com",
                msg=f"Subject:Happy Birthday\n\n{letter}")
