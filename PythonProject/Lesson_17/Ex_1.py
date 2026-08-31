"""Задание 1
Базовый класс Order. У заказа должны быть:
● номер;
● сумма;
● статус.
Реализуйте методы:
● pay()
● cancel()
Заказ нельзя отменить после оплаты. Если пользователь
пытается выполнить недопустимую операцию, должно
возникать собственное исключение: InvalidOrderStateError.
Создайте иерархию:
OrderError
└── InvalidOrderStateError
● Добавьте __str__: Объект заказа должен красиво
отображаться: Заказ #1001: 250 EUR, статус: оплачено
● Добавьте __eq__:Два заказа считаются одинаковыми,
если у них одинаковый номер."""


class OrderError(Exception):
    pass

class InvalidOrderStateError(OrderError):
    pass

class Order:
    def __init__(self, order_number: int, amount: float, currency: str = "EUR", status: str = "новый"):
        self.order_number = order_number
        self.amount = amount
        self.currency = currency
        self.status = status

    def pay(self):
        if self.status == "оплачено":
            raise InvalidOrderStateError(f"Заказ #{self.order_number} уже оплачен.")
        if self.status == "отменено":
            raise InvalidOrderStateError(f"Нельзя оплатить отмененный заказ #{self.order_number}.")

        self.status = "оплачено"
        print(f"Заказ #{self.order_number} успешно оплачен.")

    def cancel(self):
        if self.status == "оплачено":
            raise InvalidOrderStateError(f"Ошибка: Заказ #{self.order_number} нельзя отменить после оплаты.")
        if self.status == "отменено":
            print(f"Заказ #{self.order_number} уже был отменен ранее.")
            return

        self.status = "отменено"
        print(f"Заказ #{self.order_number} отменен.")

    def __str__(self):
        return f"Заказ #{self.order_number}: {self.amount} {self.currency}, статус: {self.status}"

    def __eq__(self, other):
        if not isinstance(other, Order):
            return False
        return self.order_number == other.order_number


# === ПРОВЕРКА РАБОТЫ КОДА ===

order1 = Order(1001, 250)
order2 = Order(1002, 500)
order3 = Order(1001, 999)

print("--- Проверка красивого вывода ---")
print(order1)

print("\n--- Проверка сравнения заказов ---")
print(f"Заказ 1 == Заказ 2: {order1 == order2}")
print(f"Заказ 1 == Заказ 3: {order1 == order3}")

print("\n--- Проверка обработки ошибок статуса ---")
try:
    order1.pay()
    print(order1)

    order1.cancel()

except InvalidOrderStateError as e:
    print(f"Поймали кастомное исключение -> {e}")

print(f"\nФинальное состояние заказа 1: {order1}")