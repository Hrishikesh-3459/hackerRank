#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k, m = None):
    if m == None:
        val = sum(list(map(int, list(str(n)))))
        m = val * k
        if len(str(m)) == 1:
            return m
        else:
            n = m

    if len(str(n)) == 1:
        return n
    else:
        val = sum(list(map(int, list(str(n)))))
        return superDigit((val), 0, 10)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
