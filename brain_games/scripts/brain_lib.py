import prompt


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def question_and_answer(expression, correct_answer, count):
    print(f'Question: {expression}')
    user_answer = prompt.string('Your answer: ')
    if str(user_answer) == str(correct_answer):
        print('Correct!')
        count -= 1
        is_right_answer = True
        return [is_right_answer, count]
    else:
        print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
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
