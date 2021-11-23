def main():
    girls = open('girls_name.txt', 'r', encoding='utf-8')
    boys = open('boys_name.txt', 'r', encoding='utf-8')
    user_input = input('Введите имя для поиска: ')
    general = append_list(girls, boys)
    search_(user_input, general)


def append_list(girls, boys):
    girls_list = []
    boys_list = []

    # girls
    for i in girls:
        girls_list.append(i.rstrip('\n'))

    # boys
    for j in boys:
        boys_list.append(j.rstrip('\n'))

    general_name = girls_list + boys_list
    return general_name


def search_(user_input, general_name):
    if user_input in general_name:
        print('Ваше имя находится среди популярных!')
    else:
        print('У вас обычное имя!')


main()
