#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    if (len(c) == n):
        return 0
    if (len(c) == 1):
        return n-1

    x = sorted(c)
    max_dist = max(abs(x[0] - 0), abs(x[-1] - (n-1)))
    
    i = 0
    while (i + 1 < len(c)):
        dist = abs(x[i] - x[i+1]) // 2
        if (dist > max_dist):
            max_dist = dist
        i += 1
    return max_dist



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
