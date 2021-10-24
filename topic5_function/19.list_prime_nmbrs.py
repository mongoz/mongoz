def main():
    for i in range(1, 101):
        if is_prime(i):
            print(i)


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
