#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    r = s[::-1]
    s_ascii = list(map(ord, s))
    r_ascii = list(map(ord, r))
    s_diff = []
    r_diff = []
    for i in range(1, len(s_ascii)):
        val = abs(s_ascii[i] - s_ascii[i-1])
        s_diff.append(val)
    for i in range(1, len(r_ascii)):
        val = abs(r_ascii[i] - r_ascii[i-1])
        r_diff.append(val)

    if (s_diff == r_diff):
        return "Funny"
    return "Not Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
