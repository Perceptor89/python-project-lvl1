#!/usr/bin/env python3

import random


def get_expression_with_answer():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    expression = f'{number_1} {number_2}'
    for divider in range(1, min(number_1, number_2) + 1):
        if (number_1 % divider == 0) and (number_2 % divider == 0):
            correct_answer = divider
    return [expression, correct_answer]


def game_condition():
    condition = 'Find the greatest common divisor of given numbers.'
    return condition


def main():
    print('Игру brain_gcd следует запускать из директории scripts')


if __name__ == '__main__':
    main()
