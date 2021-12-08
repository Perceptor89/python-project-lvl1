#!/usr/bin/env python3

import random


def get_expression_with_answer():
    number = random.randint(1, 100)
    i = 1
    dividers_count = 0
    while i <= number:
        if number % i == 0:
            dividers_count += 1
        i += 1
    if dividers_count == 2:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return [number, correct_answer]


def game_condition():
    condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return condition


def main():
    print('Игру brain_prime следует запускать из директории scripts')


if __name__ == '__main__':
    main()
