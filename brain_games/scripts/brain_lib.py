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
        print(f'\'{usr_answ}\' + {string} + \'{corr_answ}\'.')
        is_right_answer = False
        return [is_right_answer, count]


def ending(count: int, user_name: str):
    if count > 0:
        print(f'Let\'s try again, {user_name}!')
    else:
        print(f'Congratulations, {user_name}!')


def main():
    print('Это библиотека, которую нельзя запустить как скрипт')


if __name__ == '__main__':
    main()
