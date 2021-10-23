def main():
    for t in range(1, 11, 1):
        falling_distance(t)


def falling_distance(time):
    distance = 0.5 * 9.8 * (time ** 2)
    print(f"Дистанция за {time} ceкунд = {distance:.1f}")


main()