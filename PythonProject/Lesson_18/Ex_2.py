"""Задание 2
Есть список логов:
logs = [
"INFO: User logged in",
"ERROR: Database unavailable",
"INFO: User opened profile",
"WARNING: Slow response",
"ERROR: Connection lost",
]
Напишите генератор error_logs(), который возвращает только
сообщения с уровнем ERROR. Использование:
for log in error_logs(logs):
print(log)
Ожидается:
ERROR: Database unavailable
ERROR: Connection lost"""


def error_logs(log_list):
    """Генератор, который фильтрует логи и возвращает только ошибки."""
    for log in log_list:
        if log.startswith("ERROR:"):
            yield log


logs = [
    "INFO: User logged in",
    "ERROR: Database unavailable",
    "INFO: User opened profile",
    "WARNING: Slow response",
    "ERROR: Connection lost",
]

for log in error_logs(logs):
    print(log)