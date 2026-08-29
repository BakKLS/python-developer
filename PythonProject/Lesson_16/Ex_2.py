"""Задание 2
Небольшое задание именно на наследование и
переопределение методов. Создайте базовый класс:
Notification. У него должен быть метод: send(message).
Затем создайте:
● EmailNotification;
● SMSNotification;
● PushNotification.
Каждый класс должен по-своему реализовать send().
Проверить в цикле.
Дополнительное усложнение: добавить в Notification общий
атрибут recipient и использовать super().__init__() в дочерних
классах."""

class Notification:
    def __init__(self, recipient: str):
        self.recipient = recipient

    def send(self, message: str):
        pass

class EmailNotification(Notification):
    def __init__(self, recipient: str, subject: str = "Без темы"):
        super().__init__(recipient)
        self.subject = subject

    def send(self, message: str):
        print(f"Отправка Email на адрес {self.recipient} [Тема: {self.subject}]: {message}")

class SMSNotification(Notification):
    def __init__(self, recipient: str):
        super().__init__(recipient)

    def send(self, message: str):
        print(f"Отправка SMS на номер {self.recipient}: {message}")

class PushNotification(Notification):
    def __init__(self, recipient: str, device_id: str):
        super().__init__(recipient)
        self.device_id = device_id

    def send(self, message: str):
        print(f"Отправка Push-уведомления пользователю {self.recipient} (Device ID: {self.device_id}): {message}")


# === ПРОВЕРКА В ЦИКЛЕ ===

notifications = [
    EmailNotification("aliens123@mail.ru", "Успешный пуш"),
    SMSNotification("+375291234567"),
    PushNotification("Orex", "iPhone_114_Pro")
]

text_to_send = "Ваш код успешно отправлен на GitHub!"

print("--- Запуск рассылки уведомлений ---")
for notif in notifications:
    notif.send(text_to_send)