import random


def main():
    print(f"Игра \"Угадай число от 1 до 100!\"")
    print('Число сгенерировано.')
    generateRandom()


def generateRandom():
    again = 'Д'
    total = 1
    number = random.randint(1, 101)
    while again == 'Д':
        user_number = int(input('Ваш ответ: '))
        total += 1
        if user_number < number:
            print('Слишком мало, пробуйте ещё раз')
            again = input('Ещё попытка? (Д): ')
        elif user_number > number:
            print('Cлишком много, пробуйте ещё раз')
            again = input('Ещё попытка? (Д): ')
        elif user_number == number:
            print('Поздравляю! Вы угадали!')
    print(f'Количество догадок = {total}')


main()
