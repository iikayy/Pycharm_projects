# import smtplib
#
# my_email = "benblacck@gmail.com"
# password = "nqaonvxsembaeazn"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, to_addrs="benblacck@outlook.com", msg="Subject:Helloo\n\nThis is the body of my email")


# import datetime as dt
#
# # now = dt.datetime.now()
# # year = now.year
# # # month = now.month
# # day = now.weekday()
# # print(day)
#
#
# date_of_birth = dt.datetime(year=1957, month=7, day=28, hour=4)
# print(date_of_birth)

import datetime as dt
import random
import smtplib
now = dt.datetime.now()
today = now.weekday()
if today == 0:

    with open("quotes.txt") as file:
        quote_list = file.readlines()
        quote = random.choice(quote_list)

    my_email = "benblacck@gmail.com"
    password = "nqaonvxsembaeazn"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="benblacck@outlook.com",
            msg=f"Subject:Good morning\n\n{quote}")















