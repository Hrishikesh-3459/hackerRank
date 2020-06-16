#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    p = arr[0]
    left = []
    right = []
    equal = []
    for i in arr:
        if i == p:
            equal.append(i)
        elif i < p:
            left.append(i)
        elif i > p:
            right.append(i)
    new = left + equal + right
    return new

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
