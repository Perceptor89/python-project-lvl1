#!/usr/bin/env python3

import random


CONDITION = 'What number is missing in the progression?'


def generate_progression(prg_start, prg_difference, prg_length):
    prg = [(prg_start + i * prg_difference) for i in range(0, prg_length)]
    return prg


def generate_expression_answer():
    prg_start = random.randint(1, 20)
    prg_difference = random.randint(1, 10)
    prg_length = random.randint(5, 10)
    progression = generate_progression(prg_start, prg_difference, prg_length)
    secret_element_index = random.randint(0, prg_length - 1)
    answer = str(progression[secret_element_index])
    progression[secret_element_index] = '..'
    expression = ' '.join(map(str, progression))
    return [expression, answer]
