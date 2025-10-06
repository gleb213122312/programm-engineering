def average(*args):
    if len(args) == 0:
        print("Нет данных для вычисления.")
        return
    avg = sum(args) / len(args)
    print(f"Среднее арифметическое: {avg}")

if __name__ == "__main__":
    average(10, 20, 30, 40, 50)
