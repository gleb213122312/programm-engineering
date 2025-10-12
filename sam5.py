def process_numbers(numbers):
    result_set = set()
    for num in set(numbers):
        count = numbers.count(num)
        for i in range(1, count + 1):
            if i == 1:
                result_set.add(num)
            else:
                result_set.add(str(num) * i)
    return result_set

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

set_1 = process_numbers(list_1)
set_2 = process_numbers(list_2)
set_3 = process_numbers(list_3)

print(set_1)
print(set_2)
print(set_3)