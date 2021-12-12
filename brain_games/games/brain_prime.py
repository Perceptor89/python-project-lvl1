#!/usr/bin/env python3

import random


def is_prime(number):
    i = 1
    dividers_count = 0
    while i <= number:
        if number % i == 0:
            dividers_count += 1
        i += 1
    if dividers_count == 2:
        return True
    else:
        return False


def generate_expression_answer():
    number = random.randint(1, 100)
    if is_prime(number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return [number, answer]


CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
