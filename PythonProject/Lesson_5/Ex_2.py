# Пользователь вводит: имя файла; размер файла в мегабайтах; является ли пользователь администратором (yes/no).
# Правила:
# 1. Если файл имеет расширение .exe или .bat и пользователь не является администратором, вывести:
# Доступ запрещен: опасный файл
# 2. Если файл имеет расширение .zip или .rar, его размер меньше 100 МБ и пользователь является
# администратором, вывести:
# Архив администратора принят
# 3. Во всех остальных случаях вывести:
# Файл отправлен на проверку

file_name = input("Введите имя файла: \n").strip()
print("Выберите тип файла: Выберите тип файла из списка:\n1 - Программа (.exe)\n2 - Скрипт (.bat)\n3 - Архив (.zip)\n4 - Архив (.rar)\n5 - Другой тип")
choice = input("Введите цифру типа: \n").strip()
if choice == "1":
    file = file_name + ".exe"
elif choice == "2":
    file = file_name + ".bat"
elif choice == "3":
    file = file_name + ".zip"
elif choice == "4":
    file = file_name + ".rar"
else:
    file = file_name

try:
    file_size = int(input("Введите размер файла в мегабайтах: \n"))
except ValueError:
    print("По-моему вы не умеете читать, нужно только целое число!")
    exit()
user = input("Вы админ? Y/N: ").lower().strip()
admin = (user == "yes" or user == "y")
file_type = file.split(".")[-1]
if (file_type == "exe" or file_type == "bat") and not admin:
    print("Доступ запрещен: опасный файл")
elif (file_type == "zip" or file_type == "rar") and file_size < 100 and admin:
    print("Архив администратора принят")
else:
    print("Файл отправлен на проверку")
