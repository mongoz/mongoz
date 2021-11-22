def main():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7]
    n = int(input(' '))
    value(my_list, n)


def value(my_list, n):
    for i in my_list:
        if i > n:
            print(i, end=' ', sep=', ')


main()
