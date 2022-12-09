import random
import smtplib
import datetime as dt
import pandas

month = dt.datetime.now().month
day = dt.datetime.now().day
today = (month, day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    my_email = "template@gmail.com"
    birthday_person = birthdays_dict[today]
    with open(f"letter_templates//letter_{random.randint(1, 3)}.txt") as letter:
        content = letter.read()
        content = content.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="password")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="template@gmail.com",
            msg=f"Subject:test\n\n {content}"
        )
