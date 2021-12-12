#!/usr/bin/env python3

import random


def generate_progression(prg_start, prg_difference, prg_length):
    prg = [(prg_start + i * prg_difference) for i in range(0, prg_length)]
    return prg


def generate_expression_answer():
    # get random progression parameters
    prg_start = random.randint(1, 20)
    prg_difference = random.randint(1, 10)
    prg_length = random.randint(5, 10)
    # generate progression
    progression = generate_progression(prg_start, prg_difference, prg_length)
    # get random secret element
    secret_element_index = random.randint(0, prg_length - 1)
    answer = progression[secret_element_index]
    # hiding secret element
    progression[secret_element_index] = '..'
    # make string expression from progression
    expression = ' '.join(map(str, progression))
    return [expression, answer]


CONDITION = 'What number is missing in the progression?'
