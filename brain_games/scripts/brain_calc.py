#!/usr/bin/env python3

from brain_games.games.brain_calc import game_condition
from brain_games.games.brain_calc import get_expression_with_answer
from brain_games import brain_engine


def main():
    brain_engine.main(get_expression_with_answer, game_condition())


if __name__ == '__main__':
    main()
