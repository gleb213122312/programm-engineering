class FileLogger:
    """Декоратор-класс: логирует вызовы функций в log.txt"""

    def __init__(self, func):
        self.func = func
        self.log_file = 'log.txt'   # лог пишем сюда

    def __call__(self, *args, **kwargs):
        # логируем перед вызовом
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f'Вызов {self.func.__name__} с args={args}, kwargs={kwargs}\n')

        result = self.func(*args, **kwargs)

        # логируем после вызова
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f'Функция {self.func.__name__} завершилась.\n\n')

        return result


@FileLogger
def add_line_to_file(text):
    """Добавляет строку в data1.txt"""
    with open('data1.txt', 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    print('Строка записана в data1.txt')


@FileLogger
def show_file():
    """Печатает содержимое data1.txt"""
    print('Содержимое data1.txt:')
    with open('data1.txt', 'r', encoding='utf-8') as f:
        print(f.read())


if __name__ == '__main__':
    add_line_to_file('Это первая строка')
    add_line_to_file('Вторая строка для примера')
    show_file()
