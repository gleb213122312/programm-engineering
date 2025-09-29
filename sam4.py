s = input("Введите предложение на английском: ")

print("Длина:", len(s))
print("В нижнем регистре:", s.lower())
print("Количество гласных:", sum(s.lower().count(v) for v in "aeiou"))
print("Замена ugly -> beauty:", s.replace("ugly", "beauty"))
print("Начинается с 'The':", s.startswith("The"))
print("Заканчивается на 'end':", s.endswith("end"))
