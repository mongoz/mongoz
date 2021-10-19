days = int(input('Введите число дней: '))
population = float(input('Cтартовое число: '))
upgrade = 0.3
total = 0
upgrade_1 = 0
print('День\tПопуляция')
for i in range(1, days+1):
    print(f'{i}\t\t{population}')
    upgrade_1 = population*upgrade
    population += upgrade_1


