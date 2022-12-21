from random import randint
roulette = randint(1, 30)
def game(a,b):
    if a == roulette:
        c = b * 2
        return c
    elif a != roulette:
        c = 0
        return c

