from heron import heron_area

def main():
    print("Введите стороны треугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    result = heron_area(a, b, c)

    print(f"Площадь треугольника: {result:.2f}")

if __name__ == "__main__":
    main()
