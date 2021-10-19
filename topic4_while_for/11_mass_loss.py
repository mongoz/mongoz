mass = int(input('Масса человека: '))
months = 6
increment = 1.5
for i in range(1, months+1):
    mass -= increment
    print(f"Mасса за {i} месяц = {mass}")