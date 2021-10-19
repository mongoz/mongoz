balance = int(input())
APY = float(input())
APY_1 = APY/100
accural_frequency = int(input())
years = int(input())

balance_APY = balance*((1 + APY_1/accural_frequency)**(accural_frequency*years))

print(f"Cумма {balance}$ c процентной ставкой {APY}% за {years} лет = {balance_APY:.2f}$")