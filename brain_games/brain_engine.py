import prompt


TRIES = 3


def start(module):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    print(module.CONDITION)
    for i in range(0, TRIES):
        expression, correct_answer = module.generate_expression_answer()
        print(f'Question: {expression}')
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(correct_answer):
            print('Correct!')
        else:
            string = ' is wrong answer ;(. Correct answer was '
            print(f'\'{user_answer}\' {string} \'{correct_answer}\'.')
            print(f'Let\'s try again, {user_name}!')
            break
    else:
        print(f'Congratulations, {user_name}!')
