#!/usr/bin/env python3

import random
from brain_games.scripts import brain_lib


def get_expression_with_answer():
    expression = []
    operand = random.choice(['+', '-', '*'])
    number_1 = random.randint(1, 20)
    number_2 = random.randint(1, 20)
    if operand == '+':
        correct_answer = number_1 + number_2
        expression = [f'{number_1} + {number_2}', correct_answer]
    elif operand == '-':
        correct_answer = number_1 - number_2
        expression = [f'{number_1} - {number_2}', correct_answer]
    else:
        correct_answer = number_1 * number_2
        expression = [f'{number_1} * {number_2}', correct_answer]
    return expression


def main():
    brain_lib.greet()
    user_name = brain_lib.welcome_user()
    print('What is the result of the expression?')

    is_right = True
    count = 3
    while count > 0 and is_right is True:
        expression, corr_answ = get_expression_with_answer()
        is_right, count = brain_lib.qtn_and_answ(expression, corr_answ, count)

    brain_lib.ending(count, user_name)


if __name__ == '__main__':
    main()
