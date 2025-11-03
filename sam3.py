class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def short_info(self):
        return f"'{self.title}' — {self.author}, {self.year}"

class BookWithRating(Book):
    def __init__(self, title, author, year, rating=0.0):
        super().__init__(title, author, year)
        self.rating = rating
    def add_rating(self, value):
        self.rating = max(0, min(5, value))
    def short_info(self):
        return f"{super().short_info()}. Рейтинг: {self.rating:.1f}/5"

b = BookWithRating("Мастер и Маргарита", "М.А. Булгаков", 1967)
print(b.short_info())
b.add_rating(4.7)
print(b.short_info())
