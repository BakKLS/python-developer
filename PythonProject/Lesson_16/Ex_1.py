"""Задание 1
Создайте класс BankAccount, который представляет
банковский счёт. У объекта должны быть:
owner — имя владельца; _balance — текущий баланс.
Реализуйте методы:
● deposit(amount) — пополнение счёта;
● withdraw(amount) — снятие денег;
● get_balance() — получение текущего баланса.
Правила:
● нельзя пополнить счёт на отрицательную или нулевую
сумму;
● нельзя снять отрицательную или нулевую сумму;
● нельзя снять больше денег, чем есть на счёте.
Замените get_balance() на property.
Имеется в виду доступ через точку как атрибут ClassName.balance"""

class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            print("Ошибка: сумма пополнения должна быть больше нуля.")
        else:
            self._balance += amount
            print(f"Счёт пополнен на {amount}. Текущий баланс: {self._balance}")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Ошибка: сумма снятия должна быть больше нуля.")
        elif amount > self._balance:
            print(f"Ошибка: недостаточно средств. Доступно: {self._balance}")
        else:
            self._balance -= amount
            print(f"Снято {amount}. Текущий баланс: {self._balance}")


# === ПРОВЕРКА РАБОТЫ КОДА ===

account = BankAccount("Алексей", 1000.0)

print(f"Владелец: {account.owner}, Баланс: {account.balance}")

print("\n--- Тестируем пополнение ---")
account.deposit(500)
account.deposit(-100)

print("\n--- Тестируем снятие ---")
account.withdraw(300)
account.withdraw(2000)
account.withdraw(-50)

print(f"\nФинальный баланс через точку: {account.balance}")