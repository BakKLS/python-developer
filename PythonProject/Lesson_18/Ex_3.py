"""Задание 3
Есть интернет-магазин.
Сейчас существуют три вида скидки:
● обычная — 5%;
● постоянный клиент — 10%;
● VIP — 20%.
Нужно реализовать расчёт скидки.
Главное условие
Код расчёта заказа не должен содержать конструкцию:
if discount_type == ...
для каждого нового типа скидки.
Добавьте возможность легко создать новую стратегию
скидки.
Усложнение
Добавьте:
● скидку на день рождения;
● скидку по промокоду.
При этом существующий код расчёта заказа менять не
должен."""

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    """Абстрактный класс (интерфейс) для всех стратегий скидок."""

    @abstractmethod
    def calculate(self, price: float) -> float:
        """Принимает базовую цену, возвращает цену со скидкой."""
        pass


class RegularDiscount(DiscountStrategy):
    """Обычная скидка — 5%"""

    def calculate(self, price: float) -> float:
        return price * 0.95


class RegularCustomerDiscount(DiscountStrategy):
    """Постоянный клиент — 10%"""

    def calculate(self, price: float) -> float:
        return price * 0.90


class VIPDiscount(DiscountStrategy):
    """VIP — 20%"""

    def calculate(self, price: float) -> float:
        return price * 0.80


class Order:
    """Класс заказа. Код расчета цены НЕ меняется при добавлении новых скидок."""

    def __init__(self, amount: float, discount_strategy: DiscountStrategy):
        self.amount = amount
        self.discount_strategy = discount_strategy

    def get_total_price(self) -> float:
        return self.discount_strategy.calculate(self.amount)


class BirthdayDiscount(DiscountStrategy):
    """Скидка на день рождения — фиксированная (например, 15%). Делаю 15%."""

    def calculate(self, price: float) -> float:
        return price * 0.85


class PromoCodeDiscount(DiscountStrategy):
    """Скидка по промокоду. Принимает код и проверяет его."""

    def __init__(self, code: str):
        self.code = code

    def calculate(self, price: float) -> float:
        if self.code == "SUPER2026":
            return price * 0.75
        return price



base_amount = 10000.0
print(f"Исходная стоимость заказа: {base_amount}\n")

order1 = Order(base_amount, RegularDiscount())
print(f"Обычная скидка (5%): {order1.get_total_price()}")

order2 = Order(base_amount, VIPDiscount())
print(f"VIP скидка (20%): {order2.get_total_price()}")

order_birthday = Order(base_amount, BirthdayDiscount())
print(f"Скидка в День Рождения (15%): {order_birthday.get_total_price()}")

order_promo = Order(base_amount, PromoCodeDiscount("SUPER2026"))
print(f"Скидка по промокоду (25%): {order_promo.get_total_price()}")