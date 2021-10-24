def main():
    print('Программа проверяет простое число, либо сложное.\n')
    user_number = int(input('Введите число для проверки: '))
    status = is_prime(user_number)
    if user_number == 1:
        print('1 - не простое число.')
    else:
        if is_prime(user_number):
            print(status, '(это простое число)')
        else:
            print(status, '(это сложное число)')


def is_prime(user_number):
    status = True
    # цикла for, чтобы мы могли разделить наше число на каждое меньшее число.
    # Если он делится поровну на любое число (кроме 1 и самого себя)
    # это не простое число, поэтому status = False
    for i in range(2, user_number):
        if user_number % i == 0:
            status = False
    return status


main()
