pens = int(input('Cколько пени'))
nikel = int(input('Cколько пятицентовиков'))
dime = int(input('Cколько десятицентовиков'))
quarter = int(input('Cколько четвертаков'))

total = pens+(5*nikel)+(10*dime)+(25*quarter)

if total == 100:
    print('Поздравляю. Результат = 1$')
elif total < 100:
    print('Это меньше 1$')
else:
    print('Это больше 1$')