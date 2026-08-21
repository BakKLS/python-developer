"""Задание 3
Дана директория:
project/
data.txt
config.json
image.png
users.txt
README.md
Напишите программу, которая с помощью os.listdir():
● получает список содержимого директории;
● находит только файлы с расширением .txt;
● выводит их имена;
● считает их количество."""



import os

txt_files = [f for f in os.listdir("project") if f.endswith(".txt")]

print("Найденные файлы:", *txt_files, sep="\n")
print(f"Всего файлов: {len(txt_files)}")