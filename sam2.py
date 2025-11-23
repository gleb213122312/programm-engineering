def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    fib_200 = None

    with open("fib.txt", "w", encoding="utf-8") as f:
        for fib_200 in fib(200):
            f.write(str(fib_200) + "\n")

    print("200-е число Фибоначчи:", fib_200)
    print("Все числа с 1-го по 200-е записаны в файл fib.txt")
