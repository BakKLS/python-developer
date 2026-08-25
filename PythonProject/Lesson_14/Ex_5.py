"""Задание 5
Есть файл users.csv:
name,email,phone
Alex,alex@example.com,+375291234567
Maria,maria@test.by,+375441112233
John,john@example,+375123
Anna,anna@gmail.com,+375297778899
Программа должна:
● прочитать CSV;
● проверить каждый email с помощью регулярного
выражения;
● проверить телефон;
● вывести пользователей с некорректными данными."""

import csv
import re
import os

email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"
phone_pattern = r"^\+375\d{9}$"

print("Пользователи с некорректными данными:\n")

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "users.csv")

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        email = row["email"].strip()
        phone = row["phone"].strip()

        is_email_valid = bool(re.match(email_pattern, email))
        is_phone_valid = bool(re.match(phone_pattern, phone))

        if not is_email_valid or not is_phone_valid:
            print(f"Пользователь: {name}")

            if not is_email_valid:
                print(f"  - Некорректный email: '{email}'")
            if not is_phone_valid:
                print(f"  - Некорректный телефон: '{phone}'")
            print()