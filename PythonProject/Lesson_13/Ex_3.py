"""  Задание 3
Напишите декоратор handle_errors, который автоматически перехватывает ошибки, возникающие внутри функции.
Например, есть функция:
@handle_errors
def divide(a, b):
return a / b
Декоратор должен:
● выполнить функцию;
● если функция завершилась успешно — вернуть её результат;
● если возник ZeroDivisionError — вывести: Ошибка: деление на ноль.
● если возник ValueError — вывести: Ошибка: некорректное значение.
● в любом случае программа не должна завершаться с traceback.
Проверьте работу декоратора:
print(divide(10, 2))
print(divide(10, 0))
Ожидаемое поведение:
5.0
Ошибка: деление на ноль. Дополнительное усложнение
Сделайте так, чтобы декоратор работал не только с divide(), но
и с другими функциями:
@handle_errors
def convert_to_int(value):
return int(value)
Например:
convert_to_int("100")
convert_to_int("hello")  """


def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            return "Ошибка: деление на ноль."
        except ValueError:
            return "Ошибка: некорректное значение."
        except Exception as e:
            return f"Произошла непредвиденная ошибка: {e}"

    return wrapper


""" ПРОВЕРКА РАБОТЫ ДЕКОРАТОРА """

@handle_errors
def divide(a, b):
    return a / b

print("--- Тест divide ---")
print(divide(10, 2))
print(divide(10, 0))

@handle_errors
def convert_to_int(value):
    return int(value)


print("\n--- Тест convert_to_int ---")
print(convert_to_int("100"))
print(convert_to_int("hello"))