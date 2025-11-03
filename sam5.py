class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def short_info(self):
        return f"'{self.title}' — {self.author}, {self.year}"

class EBook(Book):
    def __init__(self, title, author, year, size_mb):
        super().__init__(title, author, year)
        self.size_mb = size_mb
    def describe(self):
        return f"Электронная книга {self.short_info()} (файл ~{self.size_mb} МБ)"

class PaperBook(Book):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages
    def describe(self):
        return f"Бумажная книга {self.short_info()} ({self.pages} стр.)"

def show(book_obj):
    print("Описание книги:", book_obj.describe())

show(EBook("Пикник на обочине", "Стругацкие", 1972, 2))
show(PaperBook("Гарри Поттер и философский камень", "Дж. К. Роулинг", 1997, 432))
