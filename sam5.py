def check_exam(grades):
    average = sum(grades) / len(grades)
    result = "Сдал" if average >= 4 else "Не сдал"
    return (grades, round(average, 2), result)


# Тест 1
test1 = [5, 4, 4, 5, 3]
result1 = check_exam(test1)
print("Тест 1")
print("Список оценок:", result1[0])
print("Средний балл:", result1[1])
print("Результат:", result1[2])
print()

# Тест 2
test2 = [2, 3, 3, 2, 3]
result2 = check_exam(test2)
print("Тест 2")
print("Список оценок:", result2[0])
print("Средний балл:", result2[1])
print("Результат:", result2[2])
print()

# Тест 3
test3 = [4, 4, 4, 4, 4]
result3 = check_exam(test3)
print("Тест 3")
print("Список оценок:", result3[0])
print("Средний балл:", result3[1])
print("Результат:", result3[2])
