class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def short_info(self):
        return f"'{self.title}' — {self.author}, {self.year}"
    def age(self, current_year):
        return current_year - self.year

b = Book("Три товарища", "Э.М. Ремарк", 1936)
print(b.short_info())
print(b.age(2025))
