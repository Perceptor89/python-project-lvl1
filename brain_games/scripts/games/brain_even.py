#!/usr/bin/env python3

import random
from brain_games.scripts import brain_lib


def get_number_with_answer():
    number = random.randint(1, 101)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return [number, correct_answer]


def main():
    brain_lib.greet()
    user_name = brain_lib.welcome_user()
    print('Answer \'yes\' if the number is even, otherwise answer \'no\'.')

    count = 3
    is_right = True
    while count > 0 and is_right is True:
        number, corr_answ = get_number_with_answer()
        is_right, count = brain_lib.qtn_and_answ(number, corr_answ, count)

    brain_lib.ending(count, user_name)


if __name__ == '__main__':
    main()
