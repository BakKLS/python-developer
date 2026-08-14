# Задание 2
# Пользователь вводит предложение.
# Необходимо написать функцию
# analyze_text(text)
# которая возвращает словарь следующего вида:
# {
# "words": ...,
# "letters": ...,
# "longest_word": …,
# "shortest_word": ...,
# "unique_words": ...
# }
# где:
# ● words — количество слов;
# ● letters — количество букв (без учета пробелов);
# ● longest_word — самое длинное слово.
# ● shortest_word — самое короткое слово;
# ● unique_words — количество различных слов без учета
# регистра.
# Запрещается использовать регулярные выражения и
# сторонние библиотеки. Нельзя использовать функцию max()


def analyze_text(text):
    words = text.split()
    letters = 0
    unique_words = []
    longest_word = words[0]
    shortest_word = words[0]

    for word in words:
        letters += len(word)

        if len(word) > len(longest_word):
            longest_word = word

        if len(word) < len(shortest_word):
            shortest_word = word

        word_low = word.lower()

        if word_low not in unique_words:
            unique_words.append(word_low)

    result = {
        "words": len(words),
        "letters": letters,
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "unique_words": len(unique_words)
    }
    return result
text = input("Введите текст: \n")

print(analyze_text(text))