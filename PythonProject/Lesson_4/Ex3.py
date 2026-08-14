# Создайте исходный список покупок: shop_list = ["хлеб", "молоко"].
# 2. Создайте его ложную копию с именем fake_copy = shop_list и независимую копию с именем true_copy =
# shop_list.copy().
# 3. Добавьте в список fake_copy элемент "сыр", а из списка true_copy удалите элемент "хлеб".
# 4. Напишите код, который с помощью операторов is и функций id() проверяет тождественность исходного списка
# shop_list с обеими копиями и выводит результаты проверок.
# 5. Выведите все три списка на экран, чтобы продемонстрировать, как изменения в одной переменной повлияли
# (или не повлияли) на остальные.

shop_list = ["хлеб", "молоко"]
fake_copy = shop_list
true_copy = shop_list.copy()
fake_copy.append("сыр")
true_copy.remove("хлеб")

print("Проверка")
print(f"shop_list is fake_copy: {shop_list is fake_copy}")
print(f"id(shop_list) == id(fake_copy): {id(shop_list)} == {id(fake_copy)}")


print(f"shop_list is true_copy: {shop_list is true_copy}")
print(f"id(shop_list) == id(true_copy): {id(shop_list)} == {id(true_copy)}")

print("Проверяем как изменения в одной переменной повлияли (или не повлияли) на остальные")
print(f"shop_list: {shop_list=}")
print(f"true_copy: {true_copy=}")
print(f"fake_copy: {fake_copy=}")


