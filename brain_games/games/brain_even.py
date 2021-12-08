#!/usr/bin/env python3

import random


def get_expression_with_answer():
    number = random.randint(1, 100)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return [number, correct_answer]


def game_condition():
    condition = 'Answer \'yes\' if the number is even, otherwise answer \'no\'.'
    return condition


def main():
    print('Игру brain_even следует запускать из директории scripts')


if __name__ == '__main__':
    main()
