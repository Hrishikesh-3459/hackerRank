#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    ans = 0
    chrs = list(set(arr[0]))
    for i in chrs:
        flag = True
        for j in arr[1:]:
            if (i not in j):
                flag = False
                break
        if (flag == True):
            ans += 1
    return ans





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
