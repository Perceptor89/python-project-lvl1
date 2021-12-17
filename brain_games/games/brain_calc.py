#!/usr/bin/env python3

import random


CONDITION = 'What is the result of the expression?'


def calc(number_1, number_2, operand):
    if operand == '+':
        return number_1 + number_2
    elif operand == '-':
        return number_1 - number_2
    elif operand == '*':
        return number_1 * number_2
    else:
        return None


def generate_expression_answer():
    operand = random.choice(['+', '-', '*'])
    number_1 = random.randint(1, 20)
    number_2 = random.randint(1, 20)
    expression = f'{number_1} {operand} {number_2}'
    answer = str(calc(number_1, number_2, operand))
    return [expression, answer]
