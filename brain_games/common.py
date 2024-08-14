import prompt

ROUND_COUNT = 3

def greet_user(game_description):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_description)
    return name

def run_game(generate_round):
    name = greet_user(generate_round['description'])
    for _ in range(ROUND_COUNT):
        question, correct_answer = generate_round['generate']()
        print(f'Question: {question}')
        answer = prompt.string("Your answer: ")
        
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print('Correct!')
    print(f'Congratulations, {name}!')
