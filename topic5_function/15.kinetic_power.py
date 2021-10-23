def main():
    mass = float(input('Введите массу в кг: '))
    speed_km = float(input('Введите скорость в км/ч: '))
    speed_seconds = speed_km * (1000 / 3600)
    kinetic_energy(mass, speed_seconds)


def kinetic_energy(mass, speed_seconds):
    kinetic = 0.5 * mass * (speed_seconds ** 2)
    print(f'Кинетическая энергия тела = {kinetic:.2f} джоулей')


main()
