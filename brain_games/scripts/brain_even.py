#!/usr/bin/env python3

import random
import prompt

ROUND_COUNT = 3

def is_even(number):
    return number % 2 == 0

def play_even_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(ROUND_COUNT):
        number = random.randint(1, 100)
        correct_answer = "yes" if is_even(number) else "no"

        print(f'Question: {number}')
        answer = prompt.string("Your answer: ")
        if answer not in ['yes', 'no'] or answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')

def main():
    play_even_game()

if __name__ == "__main__":
    main()
