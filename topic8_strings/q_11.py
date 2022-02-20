def main():
    # Пустая строка
    result = ''

    # Cтрока
    user_string = 'ОстановисьИПочувствуйЗапахРоз'
    print(user_string[0])
    # Отделяем первую букву, добавляем в пустую строку
    result = result + user_string[0]
    # Цикл начиная с 2-го символа
    for i in range(1, len(user_string)):
        # Выясняем последующая буква в верх регистре
        ch = user_string[i]
        if ch.isupper():
            # Переводим в нижний регистр
            ch = ch.lower()
            result = result + ' '
            print(result)
        result = result + ch
    print(result)


main()
