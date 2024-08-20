import prompt

ROUND_COUNT = 3


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.DESCRIPTION)

    for _ in range(ROUND_COUNT):
        question, correct_answer = game.generate_round()
        print(f'Question: {question}')
        answer = prompt.string("Your answer: ")
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
