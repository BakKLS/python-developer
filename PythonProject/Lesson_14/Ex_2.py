"""   Задание 2
Есть файл data.txt
Напишите программу, которая:
● проверяет существование файла с помощью
os.path.exists();
● если файла нет — выводит сообщение;
● если файл существует — читает его;
● создаёт директорию backup если её ещё нет;
● создаёт backup/data.txt
записывает туда содержимое исходного файла.  """


import os

if not os.path.exists("data.txt"):
    print("Ошибка: файла data.txt нет.")
else:
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()

    if not os.path.exists("backup"):
        os.mkdir("backup")

    with open("backup/data.txt", "w", encoding="utf-8") as file:
        file.write(content)

    print("Копия успешно создана в backup/data.txt!")