burn = 4.2
kcal = 0
minutes = 0
for i in range(10, 31, 5):
    kcal = i * burn
    minutes = i
    print(f'Количество сожженных калорий за {minutes} = {kcal:.1f}')
