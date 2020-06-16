#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    suma = 0
    best = 0
    sub = 0
    for i in arr:
        suma = max(i, suma + i)
        best = max(best, suma)
        if i > 0:
            sub += i
    if best == 0:
        best = max(arr)
    if sub == 0:
        sub = max(arr)
    return [best, sub]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
