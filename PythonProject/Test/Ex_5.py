# Задание 5
# products = [
# {"name": "Хлеб", "price": 70, "count": 2},
# {"name": "Молоко", "price": 120, "count": 1},
# {"name": "Сыр", "price": 350, "count": 3},
# ]
# Написать функцию, которая возвращает
# {
# "total": ...,
# "most_expensive": ...,
# "items": ...
# }
# где
# ● total — общая стоимость покупки;
# ● most_expensive — название самого дорогого товара;
# ● items — общее количество товаров.

products = [
{"name": "Хлеб", "price": 70, "count": 2},
{"name": "Молоко", "price": 120, "count": 1},
{"name": "Сыр", "price": 350, "count": 3},
]

def products_shopping(products):
    total = 0
    most_expensive = products[0]["name"]
    items = 0
    max_price = products[0]["price"]

    for product in products:
        total += product["price"] * product["count"]
        items += product["count"]
        if product["price"] > max_price:
            most_expensive = product["name"]
            max_price = product["price"]

    return {"total": total,
            "most_expensive": most_expensive,
            "items":  items
            }


print(products_shopping(products))