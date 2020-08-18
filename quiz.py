# Jelmer Mulder 
# This program will simulate a quiz of 3 doors. 

# IMPORTS
from random import randint
from random import shuffle
PRICES = ['horse', 'goat', 'goat']


# DEFINITIONS
# shuffles door prics
def doorgenerator():
    shuffle(PRICES)

# first picker
def prepicker():
    door = randint(0, 2)
    pick = PRICES[door]
    return door, pick

# quiz master will show goat door
def quizmasterspick(prenumber):
    masterspick = (prenumber + 1) % 3
    print(masterspick)


# main
if __name__ == "__main__":
    doorgenerator()
    prenumber, firstchoice = prepicker()
    prenumber = 0
    quizmasterspick(prenumber)

