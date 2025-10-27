from collections import Counter
import re

text = open("article.txt", encoding="utf-8").read().lower()
words = re.findall(r"[а-яa-z]+", text)

print("Количество слов:", len(words))

count = Counter(words)
word, freq = count.most_common(1)[0]

print("Самое частое слово:", word)
print("Количество повторений:", freq)