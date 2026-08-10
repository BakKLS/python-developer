""" Задание 2
Создайте декоратор ignore_duplicates, который не позволяет выполнить функцию два раза подряд с одинаковыми аргументами.
Пример:
@ignore_duplicates
def send_message(text):
print(f"Отправлено: {text}")
Вызовы
send_message("Привет")
send_message("Привет")
send_message("Как дела?")
send_message("Как дела?")
send_message("Привет")
должны вывести
Отправлено: Привет
Повторный вызов проигнорирован.
Отправлено: Как дела?
Повторный вызов проигнорирован.
Отправлено: Привет """

def ignore_duplicates(func):
    last_call = {"args": None, "kwargs": None}

    def wrapper(*args, **kwargs):

        if args == last_call["args"] and kwargs == last_call["kwargs"]:
            print("Повторный вызов проигнорирован.")
            return None

        last_call["args"] = args
        last_call["kwargs"] = kwargs

        return func(*args, **kwargs)

    return wrapper

@ignore_duplicates
def send_message(text):
    print(f"Отправлено: {text}")

send_message("Привет")
send_message("Привет")
send_message("Как дела?")
send_message("Как дела?")
send_message("Привет")
