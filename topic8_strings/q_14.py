def get_num():
    LOT_BALL = 69

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

    # Записать в одну строку
    file_pb3 = []
    for j in range(len(file_pb2)):
        num_set = file_pb2[j].split()
        for k in range(len(num_set)):
            file_pb3.append(int(num_set[k]))
    print(file_pb3)

    # Определяем максимально частые символы
    # Создать список для частоты каждого числа.
    # Каждый элемент списка инициализируется нулем.
    frequency = [0] * (LOT_BALL + 1)
    for i in range(len(file_pb3)):
        # Получаем следующее лотерейное число
        num = file_pb3[i]

        # Увеличить частоту этого числа.
        frequency[num] += 1

        # Функция position_of_highest_value возвращает позицию
        # самого большого значения в списке num_list.




get_num()
