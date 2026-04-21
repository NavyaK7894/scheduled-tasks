# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


##################### Extra Hard Starting Project ######################
import smtplib

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import random

MY_EMAIL = "navyasreek7894@gmail.com"
PASSWORD = "mjji xuhg hzbt uoby"

data_frame = pandas.read_csv('birthdays.csv')
data_dict = data_frame.to_dict(orient='records')
print(data_dict)
now = dt.datetime.now()
day= now.day
month = now.month
letters_list = []

for i in range(len(data_dict)):
    if data_dict[i]['day'] == day and data_dict[i]['month'] == month:

        letters_list = []

        with open("./letter_templates/letter_1.txt", "r") as f1:
            letters_list.append(f1.read())

        with open("./letter_templates/letter_2.txt", "r") as f2:
            letters_list.append(f2.read())

        with open("./letter_templates/letter_3.txt", "r") as f3:
            letters_list.append(f3.read())
        print(letters_list)

        letter = random.choice(letters_list)
        print(letter)

        letter = letter.replace("[NAME]", data_dict[i]['name'])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=data_dict[i]['email'],
                msg=f"Subject: Happy Birthday!\n\n{letter}"
            )


