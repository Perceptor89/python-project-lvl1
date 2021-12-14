#!/usr/bin/env python3

from math import sqrt
import random


CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    start = 2
    stop = int(sqrt(number)) + 1
    for i in range(start, stop):
        if number % i == 0:
            return False
    else:
        return True


def generate_expression_answer():
    number = random.randint(1, 100)
    if is_prime(number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return [number, answer]
