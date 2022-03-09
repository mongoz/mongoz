def get_num():
    file = open('pball.txt', 'r')

    # Прочитать в список
    file_pb = file.readlines()
    print(file_pb)

    file.close()

    # Перезаписать в список без доп. символов
    file_pb2 = []

    for i in range(len(file_pb)):
        file_pb[i] = file_pb[i].rstrip('\n')
        file_pb2.append(file_pb[i])
    print(file_pb2)

    # Записать в список.
    file_pb3 = []
    for j in range(len(file_pb2)):
        num_set = file_pb2[j].split()
        for k in range(len(num_set)):
            file_pb3.append(int(num_set[k]))
    print(file_pb3)
    # print(len(file_pb3))
    return file_pb3


def get_frequency(file_pb3, LOT_BALL):
    # Определяем максимально частые символы
    # Создать список для частоты каждого числа.
    # Каждый элемент списка инициализируется нулем.
    frequency = [0] * (LOT_BALL + 1)
    for i in range(len(file_pb3)):
        # Получаем следующее лотерейное число
        num = file_pb3[i]

        # Увеличить частоту этого числа.
        frequency[num] += 1

    return frequency

    # Функция position_of_highest_value возвращает позицию
    # самого большого значения в списке num_list.


def position_of_highest_value(temp_list):
    highest_value = 0
    highest_position = 0
    for i in range(len(temp_list)):
        if temp_list[i] > highest_value:
            highest_value = temp_list[i]
            highest_position = [i]

    return highest_position


def most_common(frequency):
    # Создать пустой список для позиций самых распространенных значений.
    common_sorted = []

    # Сделать копию списка freq_list.
    temp_list = []
    for item in frequency:
        temp_list.append(item)

    for i in range(len(temp_list)):
        position = position_of_highest_value(temp_list)
        common_sorted.append(position)
        temp_list[position] = -1

    # Вернуть список common_sorted.
    return common_sorted


def main():
    LOT_BALL = 69
    # Получить список всех лотерейных чисел.
    file_pb3 = get_num()

    # Получить частоту каждого числа.
    frequency = get_frequency(file_pb3, LOT_BALL)

    # Получить список наиболее распространенных значений.
    sorted_by_most_common = most_common(frequency)

    # Показать 10 наиболее распространенных чисел.
    print('10 наиболее распространенных чисел (по убыванию)')
    print('------------------------------------------------')
    for i in range(10):
        print(sorted_by_most_common[i])

    # Показать 10 наименее распространенных чисел.
    sorted_by_most_common.reverse()
    print('\n10 наиболее распространенных чисел (по возрастанию)')
    print('---------------------------------------------------')
    for i in range(1, 11):
        print(sorted_by_most_common[i])
