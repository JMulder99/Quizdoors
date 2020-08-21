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



# quiz master will show goat door
def quizmasterspick(prenumber, PRICES):
    masterspick = (prenumber + 1) % 3
    if PRICES[masterspick] == 'horse':
        masterspick = (masterspick + 1) % 3
    PRICES[masterspick] = 0
    return PRICES

# one quiz round with PrePick and SecondPick
def QuizRound(SecChoice, value):
    PRICES = doorgenerator()
    Pick = randint(0, 2)
    if SecChoice:
        PRICES = quizmasterspick(Pick, PRICES)
        Pick = (Pick + 1) % 3
        if PRICES[(Pick + 1) % 3] == 0:
            Pick = (Pick + 1) % 3

    return PRICES[Pick] == 'horse'

def RunSimulation(SecChoice, value = 0, N = 10000):
    begin = time()
    for i in range(0, N):
        if QuizRound(SecChoice, value):
            value += 1
    change = value / N
    print('When SecChoice was set {}, the picker changes are {}'.format(SecChoice, change))
    print('Duration {:.3f}'.format(time() - begin))

# main
if __name__ == "__main__":
    RunSimulation(True)
    RunSimulation(False)