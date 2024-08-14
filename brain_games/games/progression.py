import random

DESCRIPTION = 'What number is missing in the progression?'

def generate_round():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = 10
    progression = [start + step * i for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
