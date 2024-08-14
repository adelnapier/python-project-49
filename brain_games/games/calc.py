import random

DESCRIPTION = 'What is the result of the expression?'

def generate_round():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    
    if operator == '+':
        correct_answer = str(number_1 + number_2)
    elif operator == '-':
        correct_answer = str(number_1 - number_2)
    elif operator == '*':
        correct_answer = str(number_1 * number_2)
    
    question = f'{number_1} {operator} {number_2}'
    return question, correct_answer
