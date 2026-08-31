"""Задание 2
Разработайте систему отправки уведомлений
пользователям.
1. Создайте общий базовый интерфейс для уведомлений.
Отправка сообщения должна выполняться через
единый метод.
2. Реализуйте отдельные классы для:
○ Email;
○ SMS;
○ Push.
3. Каждый способ отправки должен иметь собственное
поведение.
4. Создайте функцию, которая получает список
уведомлений и отправляет через них одно сообщение.
Функция должна работать с разными типами
уведомлений через полиморфизм, без проверки
конкретного класса объекта.
5. Добавьте возможность создавать уведомление
альтернативным способом из конфигурации, например
из словаря с настройками получателя.
6. Добавьте статический метод для проверки
корректности данных получателя.
7. Создайте собственную иерархию исключений для
ошибок системы уведомлений. Предусмотрите как
минимум:
○ некорректного получателя;
○ ошибку отправки уведомления.
8. Реализуйте __str__(), чтобы объекты уведомлений
имели понятное строковое представление."""


class NotificationError(Exception):
    pass

class InvalidRecipientError(NotificationError):
    pass

class DeliveryError(NotificationError):
    pass

class Notification:
    def __init__(self, recipient: str):
        if not self.validate_recipient(recipient):
            raise InvalidRecipientError(f"Неверный получатель: {recipient}")
        self.recipient = recipient

    def send(self, message: str) -> None:
        pass

    @classmethod
    def from_config(cls, config: dict):
        return cls(config.get("recipient", ""))

    @staticmethod
    def validate_recipient(recipient: str) -> bool:
        return isinstance(recipient, str) and len(recipient) > 0

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] -> {self.recipient}"


class EmailNotification(Notification):
    @staticmethod
    def validate_recipient(recipient: str) -> bool:
        return "@" in recipient

    def send(self, message: str) -> None:
        print(f"Отправлено Email на {self.recipient}: {message}")

class SMSNotification(Notification):
    @staticmethod
    def validate_recipient(recipient: str) -> bool:
        return recipient.startswith("+")

    def send(self, message: str) -> None:
        if "ошибка" in message.lower():
            raise DeliveryError("Сеть занята, SMS не доставлено")
        print(f"Отправлено SMS на {self.recipient}: {message}")


class PushNotification(Notification):

    def send(self, message: str) -> None:
        print(f"Отправлен Push на устройство {self.recipient}: {message}")


def send_to_all(notifications_list: list, message: str):
    for notif in notifications_list:
        try:
            notif.send(message)
        except DeliveryError as e:
            print(f"Ошибка отправки через {notif}: {e}")

email = EmailNotification("Kto-to@mail.com")
sms = SMSNotification("+375339874564")

push_config = {"recipient": "device_token_12345"}
push = PushNotification.from_config(push_config)

print("--- Проверка строкового представления объектов ---")
print(email)
print(sms)

items = [email, sms, push]
print("\n--- Первая рассылка (Все успешно) ---")
send_to_all(items, "Привет! Система работает.")

print("\n--- Проверка обработки ошибок ---")

try:
    bad_email = EmailNotification("неправильный_адрес_без_собачки")
except InvalidRecipientError as e:
    print(f"Поймали ожидаемую ошибку создания: {e}")

send_to_all(items, "Внимание! Произошла критическая ошибка в системе.")