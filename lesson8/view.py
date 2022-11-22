
def menu() -> str:
    print('Меню:\n'
        '1. Создать запись\n'
        '2. Найти запись\n'
        '3. Обновить запись\n'
        '4. Удалить запись\n'
        '5. Добавить запись в файл\n'
        '6. Импорт из файла с id\n'
        '7. Импорт из файла без id\n'
        '8. Показать список\n'
        '9. Выход из меню')
    return input('Выберите действие: ')


def data() -> list:
    last_name=input('Фамилия: ')
    first_name=input('Имя: ')
    class_name=input('Класс: ')
    return last_name, first_name, class_name

def number_record():
    return int(input('Введите id: '))


