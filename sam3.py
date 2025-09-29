n = input("Введите число от 0 до 10: ")
if not n.isdigit() or not 0 <= int(n) <= 10:
    print("Ошибка")
else:
    n = int(n)
    if n <= 3: print("Диапазон: 0-3")
    elif n <= 6: print("Диапазон: 3-6")
    else: print("Диапазон: 6-10")
