"""
модуль ввода / вывода
"""

from random import randint
from os.path import exists
from pprint import pprint, pformat


def load(path_to_file=None, random=False):
    """
    функция загрузки данных, приведение к строке

    по умолчанию ручной ввод, при наличии поля
    
    path_to_file: str  -- ввод из файла по указанному пути
    random      : bool -- заполнение случайными числами

    приоритет отдаётся в порядке параметров
    """
    if path_to_file:
        if not exists(path_to_file):
            print(f'файл "{path_to_file}" не существует')
            return None
        with open(path_to_file) as outer_file:
            # вычленение всех подстрок разделённых пробелами
            result_sequence = outer_file.read().strip().split()
        return result_sequence
    elif random:
        while True:
            try:
                elements_number = int(input('введите количество элементов: '))
                if elements_number <= 0:
                    raise ValueError
                break
            except ValueError:
                print('введите корректное значение!')
        while True:
            try:
                elements_lenght = int(input('введите максимальную длину элементов: '))
                if elements_lenght <= 0:
                    raise ValueError
                break
            except ValueError:
                print('введите корректное значение!')
        
        result_sequence = tuple([str(randint(0, 10**randint(0, elements_lenght))) for i in range(elements_number)])
        return result_sequence
    else: # ручной ввод
        # получение элементов из ввода пользователем
        result_sequence = input('введите элементы через пробел:\n').strip().split()
        return result_sequence


def save(sorted_sequence, path_to_file=None):
    """
    метод сохранения, либо вывода отсортированных данных
    """
    if path_to_file:
        with open(path_to_file, 'w') as out_file:
            out_file.write(pformat(sorted_sequence, compact=True))
    else:
        pprint(sorted_sequence, compact=True)


if __name__ == '__main__':
    print(load(path_to_file='test-not-exists'))
    a = load(path_to_file='test.txt')
    b = load(random=True)
    c = load()
    print(a, b, c, sep='\n')
    save(a, path_to_file='result-from-test.txt')
    save(b)
