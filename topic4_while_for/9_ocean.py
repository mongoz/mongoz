ocean = 1.6
years = 25
total = 0
print('Год\t   Миллиметры')
for i in range(2021, 2046+1):
    total += ocean
    print(f"{i}\t{total:.1f} мм.")
