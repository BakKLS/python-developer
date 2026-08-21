"""Задание 4
Содержимое:
name,price,category
Laptop,1200,Electronics
Phone,800,Electronics
Book,25,Books
Table,300,Furniture
Напишите программу, которая:
● читает CSV;
● выводит названия всех товаров;
● находит товары дороже 500;
● считает их количество;
● выводит самый дорогой товар."""

import csv

expensive_count = 0
max_price = 0
expensive_product = ""

with open("products.csv", "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    print("Все товары в магазине:")
    for row in reader:
        name = row["name"]
        price = int(row["price"])

        print(f"- {name}")

        if price > 500:
            expensive_count += 1

        if price > max_price:
            max_price = price
            expensive_product = name

print("\n--- Результаты анализа ---")
print(f"Количество товаров дороже 500: {expensive_count}")
print(f"Самый дорогой товар: {expensive_product} ({max_price})")