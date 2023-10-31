"""
модуль сортировки
"""

def sort(sorting_sequence, place_number=0):
    """
    метод RADIX LSD
    или
    поразрядная по наименее значимой цифре
    """
    def get_digit_at_place_number(gived_element):
        if len(gived_element) < place_number + 1:
            return ''  # минимальное значение при отсутствии разряда
        return gived_element[-(place_number + 1)]
    
    if not len(sorting_sequence):  # пустая последовательность
        return sorting_sequence
    
    sort_buffer = [[sorting_sequence[0]]]  # заполнение начальным значением
    for element in sorting_sequence[1:]:
        for index, sorted_subsequence in enumerate(sort_buffer):  # перебор сохранённых значений
            if (get_digit_at_place_number(element) <
                    get_digit_at_place_number(sorted_subsequence[0])):
                # меньше текущего
                sort_buffer.insert(index, [element])
                break
            elif (get_digit_at_place_number(element) ==
                    get_digit_at_place_number(sorted_subsequence[0])):
                # равно текущему
                sorted_subsequence.append(element)
                break

        if (get_digit_at_place_number(element) >
                get_digit_at_place_number(sorted_subsequence[0])):
            # больше последнего
            sort_buffer.append([element])

    # объединение строк
    sorted_sequence = [element for subsequence in sort_buffer for element in subsequence]

    if place_number < max(map(len, sorting_sequence)):  # проверка наличия большего разряда
        sorted_sequence = sort(sorted_sequence, place_number + 1)

    return sorted_sequence
