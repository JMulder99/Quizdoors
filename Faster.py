# Jelmer Mulder
# Monty-Hall problem V2

from random import randint
from time import time

def QuizRound(SecChoice, Prices):
    Pick = randint(0, 2)
    if Pick == 1:
        MastersPick = 2
    else:
        MastersPick = 1
    if SecChoice:
        if Pick == 0:
            Pick = 2
        else:
            Pick = 0
    return Prices[Pick] == 'horse'



def RunSimulation(SecChoice, value = 0, N = 10000):
    begin = time()
    PRICES = ['horse', 'goat', 'goat']
    for runs in range(N):
        if QuizRound(SecChoice, PRICES): value += 1
    print("If SecChoice is {}, then the change of picking horse is {:.4f} in {:.3f} secs.".format(SecChoice, (value / N), time() - begin))

if __name__ == "__main__":
    RunSimulation(True)
    RunSimulation(False)