#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    x = list(s.lower())
    ch = "!@#$%^&*()-+ "
    for i in ch:
        if (i in x):
            x.remove(i)
    # print(len(set(x)))
    if (len(set(x)) == 27):
        return "pangram"
    return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
