def add_two():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)      
        result = 2 + number
        print(f"Результат: {result}")
    except (ValueError, TypeError):
        print("Неподходящий тип данных. Ожидалось число.")


if __name__ == "__main__":
    add_two()
