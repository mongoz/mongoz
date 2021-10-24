def main():
    user_money = float(input('Введите текущую сумму на счете: '))
    percentage = float(input('\nПроцентная ставка: '))
    q_month = int(input('\nВведите к-о месяцев: '))
    future_value = future_money(user_money, percentage, q_month)
    print(f'Будущая сумма на счете после {q_month} мес. = {future_value:.2f} ')


def future_money(user_money, percentage, q_month):
    future_m = user_money * ((1 + 0.01 * percentage) ** q_month)
    return future_m


main()
