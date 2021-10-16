#
# import smtplib
# my_email = "42robro@gmail.com"
# password ="O4_Romaschka_009"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="poltoratsky@gmail.com",
#         msg="Subject:Hello\n\n This is thr body of my email")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(now)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15)

#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "42robro@gmail.com"
MY_PASSWORD = "O4_Romaschka_009"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="poltoratsky@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


