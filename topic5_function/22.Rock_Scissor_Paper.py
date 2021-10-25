import random as r


def main():
    status = True
    while status:
        number = generate_random()
        user_input = int(input("Вариант 1 -'камень', 2-'ножницы' 3-'бумага':  "))
        print()
        user_choice(user_input)
        comp_choice = computer_choice(number)
        compare_(comp_choice, user_input)


def generate_random():
    number = r.randint(1, 3)
    return number


def user_choice(user_input):
    if user_input == 1:
        print('Вы выбрали Ножницы')
    if user_input == 2:
        print('Вы выбрали Камень')
    if user_input == 3:
        print('Вы выбрали Бумагу')
    return user_input


def computer_choice(number):
    if number == 1:
        print('Компьютер выбрал Ножницы!\n')
    if number == 2:
        print('Компьютер выбрал Камень!\n')
    if number == 3:
        print('Компьютер выбрал Бумага!\n')
    return number


def compare_(comp_choice, us_choice):
    print()
    # status = False
    if comp_choice == 1 and us_choice == 3:
        print("Ты проиграл. Ножницы режет бумагу.")
        # status = False
    elif comp_choice == 3 and us_choice == 1:
        print("Ты выиграл. Ножницы режут бумагу.")
        # status = False
    elif comp_choice == 1 and us_choice == 2:
        print("Ты проиграл. Камень разбивает ножницы.")
    # status = False
    elif comp_choice == 2 and us_choice == 1:
        print("Ты выиграл. Камень разбивает ножницы.")
        # status = False
    elif comp_choice == 2 and us_choice == 3:
        print("Ты выиграл. Камень оборачивает бумагу.")
        # status = False
    elif comp_choice == 3 and us_choice == 2:
        print("Ты проиграл. Камень оборачивает бумагу.")
        # status = False
    elif comp_choice == us_choice:
        print()
        print("Это ничья, попробуйте ещё раз.")
        # status = True  # Если это розыгрыш, то статус будет сигнализировать, снова сыграть.
    # return status


main()
