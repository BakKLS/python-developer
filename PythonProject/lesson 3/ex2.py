#   Пользователь вводит с клавиатуры название своего любимого города (например,"Новосибирск").
#   Напишите алгоритм, который берет первые 3 буквы города, последние 3 буквы города, склеивает их вместе и дублирует полученную комбинацию 3 раза подряд через дефис


city = input("What is your favorite city?\n ")

first_three_laters = city[:3]
last_three_laters = city[-3:]

word = first_three_laters + last_three_laters

result = "-".join([word]*3)
print(result)