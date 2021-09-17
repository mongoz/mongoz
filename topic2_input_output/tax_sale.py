kilometres = int(input("Введите пройденные километры автомобилем: "))
fuel_consumption = float(input("Расход в литрах: "))
consumption = kilometres / fuel_consumption
print(f"Расход бензина в расчете на километры пройденного автомобиле: {consumption}")