import random

DESCRIPTION = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10


def generate_round():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    progression = [start + step * i for i in range(PROGRESSION_LENGTH)]
    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
