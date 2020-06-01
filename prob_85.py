#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    ans = []
    for i, cost in enumerate(arr):
        x = m - cost
        if (x in arr[i + 1: ]):
            ans.append(i + 1)
            ind = len(arr) - arr[::-1].index(x) - 1
            ans.append(ind + 1) 
            return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
