#!/usr/bin/env python3

import random


def get_expression_with_answer():
    strt_num = random.randint(1, 20)
    leg = random.randint(1, 10)
    number_of_elements = random.randint(5, 10)
    progression = [(strt_num + i * leg) for i in range(0, number_of_elements)]
    secret_element_index = random.randint(0, number_of_elements - 1)
    correct_answer = progression[secret_element_index]
    progression[secret_element_index] = '..'
    expression = ' '.join(map(str, progression))
    return [expression, correct_answer]


def game_condition():
    condition = 'What number is missing in the progression?'
    return condition


def main():
    print('Игру brain_progression следует запускать из директории scripts')


if __name__ == '__main__':
    main()
