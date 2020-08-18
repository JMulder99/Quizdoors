# Jelmer Mulder 
# This program will simulate a quiz of 3 doors. 

# IMPORTS
from random import randint
from random import shuffle
from time import time
# DEFINITIONS
# shuffles door prics
def doorgenerator():
    PRICES = ['horse', 'goat', 'goat']
    shuffle(PRICES)
    return PRICES


# first picker
def prepicker(PRICES):
    door = randint(0, 2)
    PrePick = PRICES[door]
    return door, PrePick

# quiz master will show goat door
def quizmasterspick(prenumber, PRICES):
    masterspick = (prenumber + 1) % 3
    if PRICES[masterspick] == 'horse':
        masterspick = (masterspick + 1) % 3
    PRICES.pop(masterspick)
    return PRICES


def QuizRound(SecChoice, value):
    PRICES = doorgenerator()
    PreNum, PrePick = prepicker(PRICES)
    if (not SecChoice) and PrePick == 'horse':
        value += 1
        return value
    else:
        PRICES = quizmasterspick(PreNum, PRICES)
        if PRICES[randint(0, 1)] == 'horse':
            value += 1
            return value
        else:
            return value
def RunSimulation(SecChoice, value = 0, N = 10000):
    begin = time()
    for i in range(0, N):
        value = QuizRound(SecChoice, value)
    change = value / N
    print('When SecChoice was set {}, the picker changes are {}'.format(SecChoice, change))
    print('Duration {:.3f}'.format(time() - begin))

# main
if __name__ == "__main__":
    RunSimulation(True)
    RunSimulation(False)