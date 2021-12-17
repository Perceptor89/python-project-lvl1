#!/usr/bin/env python3

from math import sqrt
import random


CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        start = 2
        stop = int(sqrt(number)) + 1
        for i in range(start, stop):
            if number % i == 0:
                return False
        else:
            return True


def generate_expression_answer():
    expression = random.randint(1, 100)
    if is_prime(expression) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return [expression, answer]
