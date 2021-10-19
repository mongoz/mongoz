def get_distance():
    distance = float(input('Введите расстояние: '))
    return distance


def convert_dist(miles):
    convert = miles * 0.6214
    return convert


def main():
    distance = get_distance()
    print(convert_dist(distance))


main()
