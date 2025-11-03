class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def short_info(self):
        return f"'{self.title}' — {self.author}, {self.year}"

class PricedBook(Book):
    def __init__(self, title, author, year, price):
        super().__init__(title, author, year)
        self.__price = 0
        self.set_price(price)
    def set_price(self, value):
        self.__price = value if value >= 0 else 0
    def info(self):
        return f"{self.short_info()} — {self.__price} ₽"

b = PricedBook("Чистый код", "Р. Мартин", 2008, 2800)
print("Цена установлена:", b.info())
b.set_price(-5)
print("После неверной цены:", b.info())
