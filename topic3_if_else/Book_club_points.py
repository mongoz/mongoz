user_input = int(input("Количество приобретенных книг: "))
if user_input == 0:
    print('Нет книг = нет очков')
elif user_input == 2:
    print('5 очков')
elif user_input == 4:
    print('15 очков')
elif user_input == 6:
    print('30 очков')
elif user_input == 8 or user_input > 8:
    print('60 очков')