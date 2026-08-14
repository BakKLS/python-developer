def limit_calls(limit: int, message: str, default):

    def decorator(func):

        calls_count = 0

        def wrapper(*args, **kwargs):

            nonlocal calls_count

            if calls_count >= limit:
                print(message)
                return default

            calls_count += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


# --- Проверка работы  ---
print("--- Тест 1 (get_data) ---")


@limit_calls(limit=3, message="Лимит вызовов исчерпан!", default=None)
def get_data(name, age):
    print(f"Получаем данные: {name}, {age}")
    return f"{name}: {age}"


print(get_data("Иван", 20))
print(get_data("Анна", 25))
print(get_data("Петр", 30))
print(get_data("Мария", 22))


print("\n--- Тест 2 (Независимость счетчиков) ---")


@limit_calls(2, "Лимит!", 0)
def add(a, b):
    return a + b


@limit_calls(3, "Больше нельзя!", [])
def get_items(category):
    return ["item1", "item2"]



print(add(1, 2))
print(add(3, 4))
print(add(5, 6))


print(get_items("books"))
print(get_items("books"))
print(get_items("books"))
print(get_items("books"))