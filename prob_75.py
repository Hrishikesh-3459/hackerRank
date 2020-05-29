#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    di = {}
    for i in s:
        if (i in di):
            di[i] += 1
        else:
            di[i] = 1
    odd_count = 0
    for i in di.values():
        if (i % 2 != 0):
            if (odd_count > 1):
                return "NO"
            else:
                odd_count += 1
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
