years = int(input('Количество лет: '))
month = 2
total = 0
total_month = 0
average = 0

for i in range(years):
    for j in range(1, month+1):
        month_p = float(input(f'Количество осадков за {j} месяц: '))
        total += month_p
        total_month += 1

average = total/total_month

print(f"Общее количество осадков за {years} года = {total}\n"
      f"Cреднее количество осадков за {years} года в месяц = {average:.1f}")

