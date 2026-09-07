"""Задание 1
Создайте класс History, который хранит список действий
пользователя: history = History([ "login", "open_profile",
"edit_profile", "logout" ])
Сделайте объект History итерируемым. При переборе
действия должны возвращаться по одному.
for action in history:
print(action)
Усложнение: Добавьте возможность создавать несколько
независимых итераций:
for action in history:
...
for action in history:
...
Обе итерации должны начинаться с первого элемента."""


class HistoryIterator:
    """Вспомогательный класс-итератор для отслеживания текущего состояния обхода."""

    def __init__(self, actions):
        self._actions = actions
        self._index = 0

    def __next__(self):
        if self._index >= len(self._actions):
            raise StopIteration

        action = self._actions[self._index]
        self._index += 1
        return action


class History:
    """Основной класс, хранящий историю действий."""

    def __init__(self, actions):
        self._actions = list(actions)

    def __iter__(self):

        return HistoryIterator(self._actions)


history = History(["login", "open_profile", "edit_profile", "logout"])

print("--- Первая итерация ---")
for action in history:
    print(action)

print("\n--- Вторая независимая итерация ---")
for action in history:
    print(action)

print("\n--- Проверка вложенных (независимых) итераций ---")
for outer in history:
    for inner in history:
        print(f"Внешний: {outer} -> Внутренний: {inner}")
        break
