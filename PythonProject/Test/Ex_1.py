# Задание 1
# Пользователь вводит последовательность целых чисел
# через пробел.
# Например:
# 5 8 -2 10 3 8 10
# Необходимо:
# 1. получить список чисел;
# 2. вывести:
# ○ максимальное число;
# ○ минимальное число;
# ○ сумму всех положительных чисел;
# 3. вывести список уникальных чисел в порядке
# возрастания.
# Нельзя использовать max(), min() и sum().

integers = input("Введите целые числа через пробел: \n")
numbers = [int(x) for x in integers.split()]


if numbers:
    min_number = numbers[0]
    max_number = numbers[0]
    sum = 0

    for num in numbers:
        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num
        if num > 0:
            sum += num
    print(f"Максимальное число {max_number}")
    print(f"Минимальное число {min_number}")
    print(f"Сумма положительных чисел: {sum}")


    numbers_1 = list(set(numbers))
    numbers_1.sort()
    print(numbers_1)
else:
    print("Не понимаю, что считаем.")