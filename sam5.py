import re

text = open("input_6.txt", encoding="utf-8").read()
words = re.findall(r"[A-Za-zА-Яа-яЁё]+", text)

total_letters = sum(len(w) for w in words)
average_length = total_letters / len(words)
longest_word = max(words, key=len)

print("Количество слов:", len(words))
print("Общее количество букв:", total_letters)
print("Средняя длина слова:", round(average_length, 2))
print("Самое длинное слово:", longest_word)
print("Длина самого длинного слова:", len(longest_word))