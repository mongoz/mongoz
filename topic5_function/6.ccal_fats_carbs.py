def main():
    again = 'д'
    while again == 'д':
        carbs = float(input('Введите количество углеводов: '))
        fats = float(input('Введите количество жиров: '))
        calc_elements(carbs, fats)
        again = input('Хотите продолжить? ')


def calc_elements(carbs, fats):
    carbs_calc = carbs * 4
    fats_calc = fats * 9
    print(f'{carbs} грамм углеводов равно {carbs_calc} ккал.\n'
          f'{fats} грамм жиров равно {fats_calc} ккал.')


main()