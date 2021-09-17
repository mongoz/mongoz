user_input = int(input('Введите год: '))

if (user_input % 100 == 0) or (user_input % 400 == 0):
    print('Высокосный год. Февраль = 29 дней.')
elif (user_input % 100 != 0) and (user_input % 4 == 0):
    print("Выскосный год.Февраль = 29 дней. ")
else:
    print('Обычный год. Февраль = 28 дней')
