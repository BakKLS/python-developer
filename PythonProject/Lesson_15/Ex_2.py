"""Задание 2
Создайте класс Car, описывающий автомобиль.Реализуйте
приватные атрибуты для марки (__make), модели (__model) и
пробега (__mileage).
Добавьте геттер и сеттер для пробега.
В сеттере проверьте условие: пробег не может быть
отрицательным числом, а также не может уменьшаться
(новый пробег должен быть больше или равен старому)"""

class Car:
    def __init__(self, make: str, model: str, mileage: int):
        self.__make = make
        self.__model = model
        self.__mileage = mileage

    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, new_mileage: int):
        if new_mileage < 0:
            print("Ошибка: пробег не может быть отрицательным.")
        elif new_mileage < self.__mileage:
            print("Ошибка: пробег не может уменьшаться.")
        else:
            self.__mileage = new_mileage
            print(f"Пробег успешно обновлен до: {self.__mileage} км.")


my_car = Car("Toyota", "Camry", 10000)
print(f"Машина: {my_car.make} {my_car.model}, Текущий пробег: {my_car.mileage} км.")

print("\n--- Тест 1: Пробуем уменьшить пробег ---")
my_car.mileage = 5000

print("\n--- Тест 2: Пробуем ввести отрицательный пробег ---")
my_car.mileage = -100

print("\n--- Тест 3: Вводим корректный новый пробег ---")
my_car.mileage = 12500

print(f"\nИтоговый пробег в системе: {my_car.mileage} км.")