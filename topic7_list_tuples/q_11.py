def main():
    # Создать пустой двумерный список
    square = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    square_mod(square)
    _check_sq(square)


def square_mod(square):
    # Ввод пользователя
    for r in range(3):
        for c in range(3):
            user_input = int(input('Введи числа от 1 до 9: '))
            square[r][c] = user_input
        # print(square)
    return square


def _check_sq(square):
    # горизонталь
    g1 = square[0][0] + square[0][1] + square[0][2]
    g2 = square[1][0] + square[1][1] + square[1][2]
    g3 = square[2][0] + square[2][1] + square[2][2]

    # диагональ
    d1 = square[0][0] + square[1][1] + square[2][2]
    d2 = square[0][2] + square[1][1] + square[2][0]
    # вертикаль
    v1 = square[0][0] + square[1][0] + square[2][0]
    v2 = square[0][1] + square[1][1] + square[2][1]
    v3 = square[0][2] + square[1][2] + square[2][2]

    if g1 == 15 and g2 == 15 and g3 == 15 and d1 == 15 and d2 == 15 and v1 == 15 and v2 == 15 and v3 == 15:
        print('Волшебный Лоу Шу')
    else:
        print('Нет волшебства.')


main()
