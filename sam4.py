
grades_list_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades_list_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades_list_3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def process_grades(grades):
    result = []
    for grade in grades:
        if grade == 2:  
            continue
        elif grade == 3:  
            result.append(4)
        else: 
            result.append(grade)
    return result

processed_1 = process_grades(grades_list_1)
processed_2 = process_grades(grades_list_2)
processed_3 = process_grades(grades_list_3)

print("Исходный список 1:", grades_list_1)
print("Обработанный список 1:", processed_1)
print()

print("Исходный список 2:", grades_list_2)
print("Обработанный список 2:", processed_2)
print()

print("Исходный список 3:", grades_list_3)
print("Обработанный список 3:", processed_3)