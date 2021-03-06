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
def quizmasterspick(prenumber, PRICES, OPEN):
    masterspick = (prenumber + 1) % 3
    if PRICES[masterspick] == 'horse':
        masterspick = (masterspick + 1) % 3
    OPEN[masterspick] = True

# one quiz round with PrePick and SecondPick
def QuizRound(SecChoice, OPEN):
    PRICES = doorgenerator()
    Pick = randint(0, 2)
    OPEN[Pick] = True
    if SecChoice:
        quizmasterspick(Pick, PRICES, OPEN)
        for index, door in enumerate(OPEN): 
            if not door: 
                Pick = index
    return PRICES[Pick] == 'horse'

def RunSimulation(SecChoice, value = 0, N = 10000):
    begin = time()
    for i in range(0, N):
        OPEN = [False, False, False]
        if QuizRound(SecChoice, OPEN):
            value += 1
    change = value / N
    print('When SecChoice was set {}, the picker changes are {} in {:.3f} secs'.format(SecChoice, change, time() - begin))

# main
if __name__ == "__main__":
    RunSimulation(True)
    RunSimulation(False)