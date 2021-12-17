#!/usr/bin/env python3

import random


CONDITION = 'Answer \'yes\' if the number is even, otherwise answer \'no\'.'


def generate_expression_answer():
    expression = random.randint(1, 100)
    if expression % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return [expression, correct_answer]
