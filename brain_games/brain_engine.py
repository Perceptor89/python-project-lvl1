import prompt


def main(module):
    # welcome words
    print('Welcome to the Brain Games!')
    # asking the name and greeting
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))
    # type condition of the game
    print(module.CONDITION)
    # game rounds
    is_right = True
    count = 3
    while count > 0 and is_right is True:
        expression, correct_answer = module.generate_expression_answer()
        print(f'Question: {expression}')
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(correct_answer):
            print('Correct!')
            count -= 1
            is_right = True
        else:
            string = ' is wrong answer ;(. Correct answer was '
            print(f'\'{user_answer}\' {string} \'{correct_answer}\'.')
            is_right = False
    # goodbye words
    if count > 0:
        print(f'Let\'s try again, {user_name}!')
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
