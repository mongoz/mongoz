SAUSAGES = 10
BUNS = 8

peoples = int(input('Введите количество участников пикника: '))
hotdogs = int(input('Введите количество хот-догов для каждого участника: '))

number_hotdogs = peoples * hotdogs
print('Общее количество хот-догов:', number_hotdogs)

sausages_bag = number_hotdogs // SAUSAGES  # Количество упаковок для сосисок
if number_hotdogs % SAUSAGES != 0:
    sausages_bag += 1

buns_bag = number_hotdogs // BUNS  # Количество упаковок для булочек
if number_hotdogs % BUNS != 0:
    buns_bag += 1

remaining_buns = buns_bag * BUNS - number_hotdogs
remaining_sausages = sausages_bag * SAUSAGES - number_hotdogs
print(f'Остача булок {remaining_buns}')
print(f'Остача cосисок {remaining_sausages}')
print(f"min упаковок сосисок {sausages_bag}")
print(f"min упаковок сосисок {buns_bag}")
