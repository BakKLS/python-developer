# Задание 6
# Дан список студентов:
# students = [
# {"name": "Иван", "score": 82},
# {"name": "Анна", "score": 95},
# {"name": "Петр", "score": 67},
# {"name": "Мария", "score": 91},
# {"name": "Олег", "score": 73},
# {"name": "Елена", "score": 88},
# ]
# Используя функциональный стиль программирования:
# 1. оставить студентов, набравших не менее 80 баллов;
# 2. отсортировать их по убыванию результата;
# 3. получить список строк вида:
# Анна (95)
# Мария (91)
# Елена (88)
# Иван (82)


students = [
    {"name": "Иван", "score": 82},
    {"name": "Анна", "score": 95},
    {"name": "Петр", "score": 67},
    {"name": "Мария", "score": 91},
    {"name": "Олег", "score": 73},
    {"name": "Елена", "score": 88},
    ]
# 1.

good_students = filter(lambda student: student["score"] >= 80, students)

result_students = sorted(good_students, key = lambda x: x["score"], reverse = True )

result = list(map(lambda x: f"{x['name']} ({x['score']})", result_students))

print("\n".join(result))