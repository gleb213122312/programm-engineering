input_data = input("Введите через пробел последовательность чисел : ")

str_numbers = input_data.split()

numbers = [int(num) for num in str_numbers]

number_list = list(numbers)
number_tuple = tuple(numbers)

print("Список:", number_list)
print("Кортеж:", number_tuple)
