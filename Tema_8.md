# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил:
- **Студент: Конев Глеб Олегович**
- **Группа: ИВТ-23-1**

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверил:
- Ассистент кафедры информационных технологий и статистики, Ротенштрайх Татьяна Викторовна.

## Лабораторная работа №1
### Создай класс Car с атрибутами производитель и модель, создай объект этого класса и выведи информацию. В коде добавь понятные комментарии, объясняющие, что делает каждая часть.


```python
class Car:  # объявляем класс Car
    def __init__(self, make, model):  # конструктор принимает производителя и модель
        self.make = make   # сохраняем производителя в атрибуте объекта
        self.model = model # сохраняем модель в атрибуте объекта

my_car = Car("Toyota", "Corolla")  # создаём объект класса Car

```

### Результат:
![](pic/lab1.png)

## Лабораторная работа №2
### дополни класс Car из задания 1 методом, который заставляет машину “ехать” (выводит сообщение), и покажи результат в консоли.

```python
class Car:  # объявляем класс Car
    def __init__(self, make, model):  # конструктор: принимает производителя и модель
        self.make = make   # сохраняем производителя
        self.model = model # сохраняем модель

    def drive(self):  # метод класса: "поехать"
        print(f"Driving the {self.make} {self.model}")  # выводим сообщение о движении

my_car = Car("Toyota", "Corolla")  # создаём объект класса Car
my_car.drive()  # вызываем метод drive(), чтобы машина "поехала"


```
### Результат:
![](pic/lab2.png)

## Лабораторная работа №3
### создай класс-наследник ElectricCar от Car с полем ёмкости батареи и методом charge(). Затем заставь электромобиль поехать (drive()) и начать зарядку (charge()).

```python
class ElectricCar(Car):  # создаём класс-наследник от Car
    def __init__(self, make, model, battery_capacity):  # добавляем ёмкость батареи
        super().__init__(make, model)  # вызываем конструктор Car
        self.battery_capacity = battery_capacity  # сохраняем ёмкость батареи

    def charge(self):  # метод "зарядка"
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")  # сообщение о зарядке

my_electric_car = ElectricCar("Tesla", "Model S", 75)  # создаём объект ElectricCar
my_electric_car.drive()   # электромобиль "едет"
my_electric_car.charge()  # затем "заряжается"


```
### Результат:
![](pic/lab3.png)
  
## Лабораторная работа №4
### реализуй инкапсуляцию в Car: сделай защищённый атрибут производителя и приватный атрибут модели; покажи доступ к защищённому, а к приватному — недоступен; затем заставь машину поехать.

```python
# Демонстрация инкапсуляции: _protected и __private

class Car:
    def __init__(self, make, model):
        self._make = make      # защищённый атрибут
        self.__model = model   # приватный атрибут

    def drive(self):
        # доступ к полям внутри класса
        print(f"Driving the {self._make} {self.__model}")

my_car = Car("Toyota", "Corolla")

print(my_car._make)      # можно, но не рекомендуется
# print(my_car.__model)  # вызовет AttributeError

my_car.drive()           # корректный доступ через метод


```

### Результат:
![](pic/lab4.png)

## Лабораторная работа №5
### Сделай базовый класс Shape и два подкласса Rectangle и Circle с методом расчёта площади. Создай список из объектов круга и прямоугольника и с помощью цикла выведи площади всех фигур.

```python
# Базовый класс фигуры: определяем общий интерфейс area()
class Shape:
    def area(self):
        pass  # у базовой фигуры площадь не считается

# Прямоугольник — подкласс Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width      # ширина
        self.height = height    # высота
    def area(self):
        return self.height * self.width  # S = a * b

# Круг — подкласс Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius    # радиус
    def area(self):
        return 3.14 * self.radius * self.radius  # S = πr^2 (π ~ 3.14)

# Список фигур (полиморфизм: у всех есть метод area())
shapes = [Rectangle(3, 3), Circle(3)]

# Цикл вызывает area() у каждой фигуры, не зная её точный тип
for i in range(len(shapes)):
    print(shapes[i].area())

```
### Результат:
![](pic/lab5.png)

## Самостоятельная работа №1
### Создай свой класс и объект; покажи вывод в консоль.

```python
class Book:
    def __init__(self, title):
        self.title = title

b = Book("Война и мир")
print(b.title)

```
### Результат:
![](pic/sam1.png)

## Вывод: 
- Что использовано: класс Book, конструктор __init__, атрибут title, создание экземпляра.
- Что делает: создаёт книгу «Война и мир» и выводит её название.

  
## Самостоятельная работа №2
### Добавь в этот класс собственные атрибуты и методы; выведи результат работы.
```python
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

```
### Результат:
![](pic/sam2.png)

## Вывод:
- Что использовано: атрибуты title/author/year, методы short_info() и age(current_year).
- Что делает: печатает краткую строку о книге и считает её возраст на 2025 год.
  
## Самостоятельная работа №3
### Сделай наследование на базе своего класса; продемонстрируй работу потомка.

```python
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

```
### Результат:
![](pic/sam3.png)

## Вывод:
- Что использовано: наследование (BookWithRating ← Book), super(), переопределение short_info(), метод add_rating() с ограничением 0…5.
- Что делает: показывает информацию о книге без рейтинга, затем устанавливает рейтинг и печатает обновлённые данные.

## Самостоятельная работа №4
### Реализуй инкапсуляцию (защищённые/приватные данные или доступ через методы) и покажи вывод.

```python
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

```
### Результат:
![](pic/sam4.png)

## Вывод:
- Что использовано: инкапсуляция цены через приватное поле __price, метод set_price() для валидации, метод info() для вывода.
- Что делает: устанавливает цену книги, не допускает отрицательных значений (при попытке ставит 0), выводит «ценник» до и после неверной установки.
  
## Самостоятельная работа №5
### Покажи полиморфизм: несколько классов с одинаковым методом, вызови их в цикле и выведи результат.

```python
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

```
### Результат:
![](pic/sam5.png)

## Вывод:
- Что использовано: полиморфизм — два подкласса (EBook, PaperBook) с одинаковым методом describe(), функция show() вызывает его независимо от типа.
- Что делает: создаёт электронную и бумажную книги и выводит их описания одним и тем же способом.

## Общий вывод:
Итог по лабораторным 

В лабораторных я прошёл основу ООП: создал классы и объекты, добавил атрибуты/методы, применил наследование и переопределение, показал инкапсуляцию и полиморфизм. Убедился по выводу в консоль, что всё работает и код легко расширять.

Итог по самостоятельным про книги 

Я применил то же на теме книг:

создал класс и объект;

добавил атрибуты и методы (short_info, age);

сделал наследника с рейтингом и переопределением;

инкапсулировал цену и проверил валидацию;

показал полиморфизм через общий describe.
Итог: код понятный, расширяемый и удобный для повторного использования.
