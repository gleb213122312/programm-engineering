sentence = """Hello, world! Python IS the programming language of thE future. My
EMAIL is....
PYTHON is awesome!!!!"""

banned = open("input_5.txt", encoding="utf-8").read().lower().split()

print("Исходный текст:\n")
print(sentence)
print("\nПосле цензуры:\n")

s = sentence
s_low = s.lower()
chars = list(s)

for w in banned:
    w = w.lower()
    start = 0
    while True:
        i = s_low.find(w, start)
        if i == -1:
            break
        for j in range(i, i + len(w)):
            chars[j] = "*"
        start = i + 1  # разрешаем перекрывающиеся вхождения

censored = "".join(chars)
print(censored)
