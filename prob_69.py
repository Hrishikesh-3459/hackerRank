#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    for i in set(b):
        if (i != '_' and b.count(i) == 1):
            return 'NO'

    if (b.count('_') == 0):
        for i in range(1,len(b) - 1):
            if ((b[i-1] != b[i]) and (b[i+1] != b[i])):
                return "NO"
    return "YES"
    # Commented solution fails one case
    #if (b.count('_') == len(b)):
    #    return 'YES'
    #if (len(b) == 1 and b.isalpha()):
    #    return 'NO'
    #if (b.count('_') == 0):
    #    if (b[-1] != b[-2]):
    #       return 'NO'
    #    i = 0
    #    while (i + 1 < len(b)):
    #        if (b[i] != b[i+1]):
    #            return 'NO'
    #        i += 2

    #cols = {}
    #for i in b:
    #    if (i.isalpha()):
    #        if (i in cols):
    #            cols[i] += 1
    #        else:
    #            cols[i] = 1
    #for i in cols:
    #    if (cols[i] == 1):
    #        return 'NO'

    #return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
