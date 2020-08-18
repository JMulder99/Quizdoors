# Jelmer Mulder 
# This program will simulate a quiz of 3 doors. 

# IMPORTS
from random import randint
from random import shuffle

# DEFINITIONS
# shuffles door prics
def doorgenerator(PRICES):
    shuffle(PRICES)


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

def loop(PRICES, SecChoice, value):
    doorgenerator(PRICES)
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

# main
if __name__ == "__main__":
    SecChoice = True
    value = 0
    N = 10000
    for i in range(0, N):
        PRICES = ['horse', 'goat', 'goat']
        value = loop(PRICES, SecChoice, value)
    change = value / N
    print('When SecChoice was set {}, the picker changes are {}'.format(SecChoice, change))

    SecChoice = False
    value = 0
    N = 100
    for i in range(0, N):
        PRICES = ['horse', 'goat', 'goat']
        value = loop(PRICES, SecChoice, value)
    change = value / N
    print('When SecChoice was set {}, the picker changes are {}'.format(SecChoice, change))


