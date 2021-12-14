#!/usr/bin/env python3

import random


CONDITION = 'Find the greatest common divisor of given numbers.'


def gcd(number_1, number_2):
    for divider in range(1, min(number_1, number_2) + 1):
        if (number_1 % divider == 0) and (number_2 % divider == 0):
            gcd = divider
    return gcd


def generate_expression_answer():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    expression = f'{number_1} {number_2}'
    answer = gcd(number_1, number_2)
    return [expression, answer]
