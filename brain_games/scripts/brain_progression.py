#!/usr/bin/env python3

from brain_games.common import run_game
from brain_games.games.progression import generate_round, DESCRIPTION

def main():
    run_game({'generate': generate_round, 'description': DESCRIPTION})

if __name__ == "__main__":
    main()

