def main():
    m, total, average = list_mod()
    print(sum(m))
    print(len(m))
    print(f'Min: {min(m)}\n'
          f'Max: {max(m)}\n'
          f'Total: {total:.2f}\n'
          f'Average: {average:.2f}')


def list_mod():
    m = []
    total = 0
    for i in range(1, 21):
        u_input = int(input(f'Введите {i}-е число: '))
        total += u_input

        m.append(u_input)

    average = total / len(m)
    return m, total, average


main()
