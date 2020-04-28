from itertools import cycle

def saveThePrisoner(n, m, s):
    return((s - 2 + m) % n + 1)

print(saveThePrisoner(5,2,1))