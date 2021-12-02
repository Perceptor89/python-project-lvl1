#!/usr/bin/env python3

import random
from brain_games.scripts import brain_lib


def get_expression_with_answer():
    number = random.randint(1, 101)

    is_prime = True
    i = 2
    while is_prime is True and i < number:
        if number % i != 0:
            i += 1
        else:
            is_prime = False

    if is_prime is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return [number, correct_answer]


def main():
    brain_lib.greet()
    user_name = brain_lib.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    is_right_answer = True
    count = 3
    while count > 0 and is_right_answer is True:
        expression, correct_answer = get_expression_with_answer()
        is_right_answer, count = brain_lib.question_and_answer(expression, correct_answer, count)

    brain_lib.ending(count, user_name)


if __name__ == '__main__':
    main()
