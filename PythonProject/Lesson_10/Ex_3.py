# Задание 3
# Дана строка
# text = "functional programming"
# Создайте словарь, где ключ — символ, значение — количество
# его появлений.
# Пробелы учитывать не нужно.


from collections import Counter

text = "functional programming"

clean_text = text.replace(" ", "")

char_counts = dict(Counter(clean_text))

print(char_counts)