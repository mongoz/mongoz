def text_calc_V(text):
    VOW = 0
# Гласные
    vowels = 'AEIOU'

    for i in text:
        if i.upper() in vowels:
            VOW += 1
    return VOW


def text_calc_C(text):
    CONST = 0
# Cогласные
    constants = 'BCDFGHJKLMNPQRSTVWXYZ'

    for i in text:
        if i.upper() in constants:
            CONST += 1
    return CONST


def main():
    text = input('Enter string')
    V = text_calc_V(text)
    C = text_calc_C(text)
    print(f"Гласные {V}\n"
          f"Согласные {C}")


main()