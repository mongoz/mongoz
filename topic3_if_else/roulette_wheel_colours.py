user_input = int(input('Номер кармана от 0 до 36: '))

if 1 <= user_input <= 10:
    if user_input % 2 != 0:
        print('Красный')
    else:
        if user_input % 2 == 0:
            print('Черный')
elif 11 <= user_input <= 18:
    if user_input % 2 != 0:
        print('Черный')
    else:
        if user_input % 2 == 0:
            print('Красный')
elif 19 <= user_input <= 28:
    if user_input % 2 != 0:
        print('Красный')
    else:
        if user_input % 2 == 0:
            print('Черный')
elif user_input >= 29 and user_input <= 36:
    if user_input % 2 != 0:
        print('Черный')
    else:
        if user_input % 2 == 0:
            print('Красный')
else:
    print('Введите верное число')