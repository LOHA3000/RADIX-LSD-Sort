"""
модуль интерфейса
"""

import sort
import input_output
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from os import getcwd as current_path


class Interface:
    """
    класс с функциями управления интерфейсом
    """
    def __init__(self):
        """
        инициализация объекта класса,
        загрузка последовательности
        """
        self.entered_sequence = self.load_sequence()
        self.result_sequence = []

    def load_sequence(self):
        """
        функция загрузки массива
        """
        while True:
            load_way = input('выберите способ ввода:\n'
                             '\tf -- из файла\n'
                             '\tr -- случайные\n'
                             '\tk -- с клавиатуры\n>>> ').lower()
            if load_way not in ('f', 'r', 'k'):
                print('выберите один из предложенных способов!')
                continue
            else:
                break
        if load_way == 'f':
            loaded_sequence = input_output.load(askopenfilename(title='файл с последовательностью',
                                                                initialdir=current_path()))
        elif load_way == 'r':
            loaded_sequence = input_output.load(random=True)
        elif load_way == 'k':
            loaded_sequence = input_output.load()
            
        return loaded_sequence

    def sort_sequence(self):
        """
        метод сортировки загруженного массива
        """
        self.result_sequence = sort.sort(self.entered_sequence)

    def save_sorted_sequence(self):
        """
        метод сохранения отсортированного массива
        """
        if not len(self.result_sequence):
            print('последовательность не отсортирована!')
        save = input('сохранить? y/n: ').lower()
        if save in ('да', 'y', 'yes'):
            input_output.save(self.result_sequence,
                              asksaveasfilename(title='сохранение результата',
                                                initialdir=current_path()))
        else:
            input_output.save(self.result_sequence)
        


if __name__ == '__main__':    
    help(sort)
    help(input_output)
    help(Interface)

    root = Tk()
    
    app = Interface()
    app.sort_sequence()
    app.save_sorted_sequence()

    root.destroy()
    
