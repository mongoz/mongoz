def main():
    # Прочитать
    file = open('charge_accounts.txt', 'r', encoding='utf-8')
    _search_deploy(_append(file))


def _append(file):
    # Cоздать пустой список
    values = []
    # Добавить значения в список
    for i in file:
        values.append(int(i))
    # Вывод для проверки содержимого
    print(values)
    return values


def _search_deploy(values):
    try:
        # Ввод пользователя и поиск
        user_input = int(input('Номер расчетного счета: '))
    except ValueError as err:
        print(err)
        user_input = int(input('Номер расчетного счета: '))

    if user_input not in values:
        print('Недопустимый номер счета')
    else:
        print('Допустимый номер счета')


main()
