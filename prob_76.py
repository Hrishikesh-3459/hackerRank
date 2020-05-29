#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    arr_d = {}
    brr_d = {}
    for i in arr:
        if (i in arr_d):
            arr_d[i] += 1
        else:
            arr_d[i] = 1
    for i in brr:
        if (i in brr_d):
            brr_d[i] += 1
        else:
            brr_d[i] = 1
    ans = []
    for i in brr:
        if (i not in arr or brr_d[i] != arr_d[i]):
            ans.append(i)
    fin_ans = sorted(list(set(ans)))
    return fin_ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
