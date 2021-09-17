user_mass = float(input('Вес: '))
user_heights = float(input('Рост: '))

index_mass = (user_mass / user_heights)*100
print(f'Индекс массы = {index_mass:.2f}')
if 18.5 <= index_mass <= 25:
    print('Оптимально')
elif index_mass < 18.5:
    print('Ниже нормы')
else:
    if index_mass > 25:
        print('Выше нормы')

