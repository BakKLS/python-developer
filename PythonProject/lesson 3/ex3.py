# 1. Создайте словарь hero со следующей структурой: {"name": "Gandalf", "level": 80, "inventory": ["staff", "robe", "potion"]}
# 2. Добавьте в инвентарь (список внутри словаря) новый предмет "sword" с помощью списочного метода.
# 3. Перезапишите уровень персонажа, увеличив его текущее значение ровно на 1.
# 4. Добавьте в словарь новый ключ "guild" со значением "Wizards".
# 5. Выведите финальное состояние словаря в консоль.


hero = {
    "name": "Gandalf",
    "level": 80,
    "inventory": ["staff", "robe", "potion"]
}

hero["inventory"].append("sword")
hero["level"] += 1
hero["guild"] = "Wizards"
print(hero)

