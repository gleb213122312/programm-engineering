def fib(n):
    a, b = 1, 1
    for _ in range(n):      
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    fib_200 = None

    for fib_200 in fib(200):
        pass

    print(fib_200)
