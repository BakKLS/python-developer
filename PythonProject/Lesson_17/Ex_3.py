"""Задание 3
Создайте класс Item, представляющий предмет в инвентаре
персонажа.
Каждый предмет имеет:
● name — название;
● weight — вес;
● price — стоимость.
Необходимо перегрузить операторы:
● + — объединяет два предмета в «набор» и возвращает
их общую стоимость;
● < — сравнивает предметы по весу;
● == — считает предметы одинаковыми, если совпадают
их названия;
● str() — выводит предмет в удобном формате.
Дополнительное усложнение(необязательно)
Добавьте класс Inventory и перегрузите оператор +, чтобы
можно было написать:
inventory + sword
и получить новый инвентарь, содержащий исходные
предметы и меч."""

class Item:
    def __init__(self, name: str, weight: float, price: int):
        self.name = name
        self.weight = weight
        self.price = price

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Item):
            return self.weight < other.weight
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.name == other.name
        return False

    def __str__(self) -> str:
        return f"{self.name} (Вес: {self.weight} кг, Цена: {self.price} золота)"


class Inventory:
    def __init__(self, items_list=None):
        if items_list is None:
            self.items = []
        else:
            self.items = list(items_list)

    def __add__(self, other):
        if isinstance(other, Item):
            new_items_list = self.items + [other]
            return Inventory(new_items_list)
        return NotImplemented

    def __str__(self) -> str:
        if not self.items:
            return "Инвентарь пуст."

        content = ", ".join(item.name for item in self.items)
        return f"Инвентарь: [{content}]"

sword = Item("Стальной меч", weight=5.5, price=150)
shield = Item("Железный щит", weight=8.0, price=100)
potion = Item("Зелье лечения", weight=0.5, price=50)
fake_sword = Item("Стальной меч", weight=1.2, price=20)


print("--- Проверка __str__ ---")
print(sword)
print(shield)

print("\n--- Проверка оператора + (Общая стоимость) ---")
total_price = sword + shield
print(f"Общая стоимость меча и щита: {total_price} золота")

print("\n--- Проверка оператора < (Сравнение по весу) ---")
print(f"Меч легче щита? {sword < shield}")
print(f"Щит легче зелья? {shield < potion}")

print("\n--- Проверка оператора == (Равенство по имени) ---")
print(f"Меч равен фейк-мечу? {sword == fake_sword}")
print(f"Меч равен щиту? {sword == shield}")


print("\n--- Проверка усложнения с Инвентарем ---")
my_inventory = Inventory()
print(my_inventory)

inventory_with_sword = my_inventory + sword
final_inventory = inventory_with_sword + shield

print("Исходный инвентарь не изменился:", my_inventory)
print("Финальный инвентарь содержит предметы:", final_inventory)