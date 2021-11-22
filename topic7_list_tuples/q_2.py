import random


def main():
    NUM = 7
    my_list = []
    for i in range(NUM):
        my_list.append(random.randint(0, 9))
    for i in my_list:
        print(i)


main()
