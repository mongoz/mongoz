A_PRICE = 20
B_PRICE = 15
C_PRICE = 10


def main():
    tickets_A = int(input("Количество проданных билетов группы A: "))
    tickets_B = int(input("Количество проданных билетов группы B: "))
    tickets_C = int(input("Количество проданных билетов группы C: "))
    calc_tickets(tickets_A, tickets_B, tickets_C)


def calc_tickets(tickets_A, tickets_B, tickets_C):
    total = (tickets_A * A_PRICE) + (tickets_B * B_PRICE) + (tickets_C * C_PRICE)
    print(f'Общая стоимость билетов составляет ${total}')


main()