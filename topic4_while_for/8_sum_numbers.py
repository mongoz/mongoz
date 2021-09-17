number = float(input('Введите + число: '))
total = 0
while number >= 0:
    total += number
    number = float(input('Введите + число: '))

print(f'Cумма чисел равна {total}')
