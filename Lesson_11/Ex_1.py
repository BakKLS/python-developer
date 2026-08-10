
""" Задание 1
Напишите функцию power_factory(power), которая возвращает новую функцию.
Возвращаемая функция должна принимать число x и возводить его в степень power, которая была передана при создании замыкания.
Пример работы:
square = power_factory(2)
cube = power_factory(3)
print(square(5)) # 25
print(cube(2)) # 8
print(square(10)) # 100
Требования:
● Использовать замыкание.
● Переменная power должна быть захвачена внутренней
функцией.
● Не использовать глобальные переменные. """


def power_factory(power):

    def nth_power(x):

        return x ** power


    return nth_power

square = power_factory(2)
cube = power_factory(3)

# Тестируем вызовы
print(square(5))
print(cube(2))
print(square(10))