#!/usr/bin/env python3

from brain_games.games import brain_calc
from brain_games import brain_engine


def main():
    brain_engine.start(brain_calc)


if __name__ == '__main__':
    main()
