#!/usr/bin/env python3

import prompt
import random


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def question_and_answer(int):
    print(f'Question: {int}')
    answer = prompt.string('Your answer: ')
    return answer


def is_even(int):
    if int % 2 > 0:
        return False
    else:
        return True


def yes_or_no(string):
    if string == 'yes':
        return 'no'
    else:
        return 'yes'


def even_game_core(user_name: str):
    number = random.randint(0, 100)
    answer = question_and_answer(number)
    even_chk = is_even(number)
    if (even_chk and answer == 'yes') or (not even_chk and answer == 'no'):
        print('Correct!')
        return True
    else:
        correct_answer = yes_or_no(answer)
        print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'')
        print(f'Let\'s try again, {user_name}!')
        return False


def even_game_structure(tries: int, user_name: str):
    print('Answer \'yes\' if the number is even, otherwise answer \'no\'')
    count = tries
    may_continue = True
    while count > 0 and may_continue is True:
        may_continue = even_game_core(user_name)
        count -= 1
    if may_continue is True:
        print(f'Congratulations, {user_name}!')


def main():
    greet()
    even_game_structure(3, welcome_user())


if __name__ == '__main__':
    main()
