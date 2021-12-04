#!/usr/bin/env python3

import random
from brain_games.scripts import brain_lib


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


def main():
    brain_lib.greet()
    user_name = brain_lib.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    is_right = True
    count = 3
    while count > 0 and is_right is True:
        expression, corr_answ = get_expression_with_answer()
        is_right, count = brain_lib.qtn_and_answ(expression, corr_answ, count)

    brain_lib.ending(count, user_name)


if __name__ == '__main__':
    main()
