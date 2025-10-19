def most_common_digits(digits_str):
    counts = {}

    for ch in digits_str:
        num = int(ch)
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    top3 = dict(sorted_counts[:3])

    print("Строка:", digits_str)
    print("Три самых популярных цифры:", list(top3.keys()))

    print("Значения по возрастанию ключа:")
    for key in sorted(top3):
        print(f"{key}: {top3[key]}")

    print("Словарь:", top3)


digits = "012345678909876543210123456789000"

most_common_digits(digits)
