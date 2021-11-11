def display_player():
    file = open('golf.txt', 'r', encoding='utf-8')
    print()
    print('Информация о игроках')
    print('********************')
    print()
    print(f'Имя\t\tРезультат')
    print("-----------------")
    for i in file:
        print(i)
    file.close()


def main():
    display_player()


main()
