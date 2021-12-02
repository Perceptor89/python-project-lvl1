#!/usr/bin/env python3

import random
from brain_games.scripts import brain_lib


def get_expression_with_answer():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    expression = f'{number_1} {number_2}'
    if number_1 < number_2:
        low_number = number_1
    else:
        low_number = number_2
#    print(f'low_number = {low_number}')
    for divider in range(1, low_number + 1):
#        print(f'divider = {divider}')
        if (number_1 % divider == 0) and (number_2 % divider == 0):
#            print(f'%1 = {number_1 % divider}' + f'%2 = {number_2 % divider}')
#            print(f'new_correct_answer = {divider}')
            correct_answer = divider
#    print(f'correct_answer = {correct_answer}')
    return [expression, correct_answer]


def main():
    brain_lib.greet()
    user_name = brain_lib.welcome_user()
    print('Find the greatest common divisor of given numbers.')

    is_right_answer = True
    count = 3
    while count > 0 and is_right_answer is True:
        expression, correct_answer = get_expression_with_answer()
        is_right_answer, count = brain_lib.question_and_answer(expression, correct_answer, count)

    brain_lib.ending(count, user_name)


if __name__ == '__main__':
    main()
