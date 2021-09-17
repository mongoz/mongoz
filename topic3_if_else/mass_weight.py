m = int(input("Введите массу: "))
CONST = 9.8
weight = m*CONST

if weight > 500:
    print('Тело слишком тяжелое')
elif weight < 100:
    print('Тело слишком легкое')
