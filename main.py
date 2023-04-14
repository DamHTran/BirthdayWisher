import pandas as pd
from datetime import datetime
import random
# ------------------------- LOAD CSV FILE ------------------------#
birthdays = pd.read_csv("birthdays.csv")
print(birthdays)

# ------------- CHECK IF TODAY IS ANYONE'S BIRTHDATE ------------#
current_day = datetime.now().day
current_month = datetime.now().month
for index, row in birthdays.iterrows():
    if row["month"] == current_month and row["day"] == current_day:
        # ------------ CHOOSE RANDOM TEMPLATE AND REPLACE NAME --------- #
        letter_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_number}.txt", "r") as file:
            letter_template = file.read()

        letter = letter_template.replace("[NAME]", row["name"])
        print(letter)

        with open(f"letter_{row['name']}.txt", "w") as file:
            file.write(letter)


# ------------------ SEND EMAIL -------------------------------#

