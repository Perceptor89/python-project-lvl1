from types import FunctionType
import prompt


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def qtn_and_answ(expression, corr_answ, count):
    print(f'Question: {expression}')
    usr_answ = prompt.string('Your answer: ')
    if str(usr_answ) == str(corr_answ):
        print('Correct!')
        count -= 1
        is_right_answer = True
        return [is_right_answer, count]
    else:
        string = ' is wrong answer ;(. Correct answer was '
        print(f'\'{usr_answ}\' {string} \'{corr_answ}\'.')
        is_right_answer = False
        return [is_right_answer, count]


def ending(count: int, user_name: str):
    if count > 0:
        print(f'Let\'s try again, {user_name}!')
    else:
        print(f'Congratulations, {user_name}!')


def main(game_expression_with_answer: FunctionType, condition: str):
    greet()
    user_name = welcome_user()
    print(condition)

    is_right = True
    count = 3
    while count > 0 and is_right is True:
        expression, corr_answ = game_expression_with_answer()
        is_right, count = qtn_and_answ(expression, corr_answ, count)

    ending(count, user_name)


if __name__ == '__main__':
    main()
