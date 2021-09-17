day = int(input())
if 1 <= day <= 7:
    if day == 1:
        print('Понедельник')
    elif day == 2:
        print('Вторник')
    elif day == 3:
        print('Среда')
    elif day == 4:
        print('Четверг')
    elif day == 5:
        print('Пятница')
    elif day == 6:
        print('Cуббота')
    elif day == 7:
        print('Воскресенье')
else:
    print('Число вне диапазона.')

