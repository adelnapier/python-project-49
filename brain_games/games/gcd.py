import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    correct_answer = str(gcd(number_1, number_2))
    question = f'{number_1} {number_2}'
    return question, correct_answer
