# Задание 3
# Пользователь может ввести пароль не более пяти раз.
# Правильный пароль:
# password = "Python2026"
# Программа должна:
# ● использовать цикл while;
# ● считать количество попыток;
# ● если введён правильный пароль — вывести Доступ
# разрешён.
# и завершить программу;
# ● если введено слово
# exit
# немедленно завершить программу;
# ● если попытки закончились — Аккаунт заблокирован.

password_correct = "Python2026"
attempt = 1
max_attempt = 5

print("Добро пожаловать. Для выхода необходимо ввести: exit\n")

while attempt <= max_attempt:
    user_password = input("Введите пароль:\n").strip()
    if user_password == "exit":
        print("Программа завершена.")
        break
    if user_password == password_correct:
        print("Доступ разрешен.")
        break
    remaining_attempts = max_attempt - attempt
    if remaining_attempts > 0:
        print(f"Пароль неверный, повторите попытку. Осталось: {remaining_attempts}")
    attempt += 1
else:
    print("Аккаунт заблокирован.")