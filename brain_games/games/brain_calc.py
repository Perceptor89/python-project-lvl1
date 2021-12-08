#!/usr/bin/env python3

import random


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


def game_condition():
    condition = 'What is the result of the expression?'
    return condition


def main():
    print('Игру brain_calc следует запускать из директории scripts')


if __name__ == '__main__':
    main()
