with open('input_1.txt', 'a+') as f:
    f.write('\nMy name is Gleb')

with open('input_1.txt', 'r') as f:
    result = f.readlines()
    print(result)