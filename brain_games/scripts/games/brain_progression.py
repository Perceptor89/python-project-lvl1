#!/usr/bin/env python3

import random
from brain_games.scripts import brain_lib


def get_expression_with_answer():
    strt_num = random.randint(1, 20)
    leg = random.randint(1, 10)
    number_of_elements = random.randint(5, 10)
    progression = [(strt_num + i * leg) for i in range(0, number_of_elements)]
    secret_element_index = random.randint(0, number_of_elements - 1)
    correct_answer = progression[secret_element_index]
    progression[secret_element_index] = '..'
    expression = ' '.join(map(str, progression))
    return [expression, correct_answer]


def main():
    brain_lib.greet()
    user_name = brain_lib.welcome_user()
    print('What number is missing in the progression?')

    is_right = True
    count = 3
    while count > 0 and is_right is True:
        expression, corr_answ = get_expression_with_answer()
        is_right, count = brain_lib.qtn_and_answ(expression, corr_answ, count)

    brain_lib.ending(count, user_name)


if __name__ == '__main__':
    main()
