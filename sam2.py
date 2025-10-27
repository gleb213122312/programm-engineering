while True:
    print("1) Добавить расход")
    print("2) Показать расходы")
    print("3) Выход")
    choice = input("Выбор: ")

    if choice == "1":
        date = input("Дата: ")
        category = input("Категория: ")
        amount = input("Сумма: ")
        note = input("Примечание: ")
        f = open("expenses.txt", "a", encoding="utf-8")
        f.write(f"{date},{category},{amount},{note}\n")
        f.close()
    elif choice == "2":
        for line in open("expenses.txt", encoding="utf-8"):
            print(line.strip())
    elif choice == "3":
        break