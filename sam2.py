def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

            if not content.strip():         
                raise ValueError('файл пустой')

            print(f'Содержимое файла "{filename}":')
            print(content)

    except ValueError as ex:
        print(f'Исключение: {ex}')
    except FileNotFoundError:
        print(f'Файл "{filename}" не найден')
    finally:
        print(f'Проверка файла "{filename}" завершена.\n')


if __name__ == '__main__':
    read_file('empty.txt')
    read_file('data.txt')
