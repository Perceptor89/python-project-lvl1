#!/usr/bin/env python3

from brain_games.games.brain_gcd import game_condition
from brain_games.games.brain_gcd import get_expression_with_answer
from brain_games import brain_engine


def main():
    brain_engine.main(get_expression_with_answer, game_condition())


if __name__ == '__main__':
    main()
