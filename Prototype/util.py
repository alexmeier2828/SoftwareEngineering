from random import randint

def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp

def shuffle(l):
    last = len(l) - 1
    for i in range(0, len(l)):
        swap(l, i, randint(0, last))

    