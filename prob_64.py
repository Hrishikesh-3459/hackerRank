#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    if (len(a) == len(set(a))):
        return -1
    ans = {}
    mis_dist = []
    for i in range(len(a)):
        if (a[i] not in ans):
            ans[a[i]] = i 
        else:
            val = (i - ans[a[i]])
            mis_dist.append(val)
    return min(mis_dist)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
