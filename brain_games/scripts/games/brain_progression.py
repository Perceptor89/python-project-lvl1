#!/usr/bin/env python3

import random
from brain_games.scripts import brain_lib


def get_expression_with_answer():
    start_number = random.randint(1, 21)
    expression = f'{start_number}'
    leg_value = random.randint(1, 10)
    number_of_elements = random.randint(5, 11)
    secret_element = random.randint(1, number_of_elements + 1)
    for i in range(1, number_of_elements + 1):
        if secret_element == i:
            correct_answer = start_number + i * leg_value
            current_symbol = '..'
            expression += f' {current_symbol}'
        else:
            current_symbol = start_number + i * leg_value
            expression += f' {current_symbol}'
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
