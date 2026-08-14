def repeat(times: int, separator: str):

    def decorator(func):

        def wrapper(*args, **kwargs):

            results = []

            for _ in range(times):
                res = func(*args, **kwargs)
                results.append(str(res))

            return separator.join(results)

        return wrapper

    return decorator


# --- Проверка работы ---

@repeat(times=3, separator="---")
def greet(name):
    return f"Привет, {name}!"


print(greet("Иван"))
print()


@repeat(times=2, separator="\n=\n")
def add(a, b):
    return a + b


print(add(5, 3))