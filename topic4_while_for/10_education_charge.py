edu_cost = 45000
years = 5
up_cost = edu_cost * 0.03
semestr = 2*years
cost_semestr = 0

while years != 0:
    edu_cost += up_cost
    years -= 1

cost_semestr = edu_cost/semestr
print(f"Общая сумма за 5 лет з учётом повышения стоимости на {up_cost}р./год = {edu_cost} р.")
print(f"Цена за семестр = {cost_semestr} рублей")

