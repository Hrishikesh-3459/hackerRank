#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    # x = list(map(s.count, s))
    # y = list(map(lambda i: i == 1, x))
    # if (all(y) == True):
    #     return "YES"
    di = {}
    for i in s:
        if (i in di):
            di[i] += 1
        else:
            di[i] = 1
    
    freq_di = {}
    for i in di:
        if (di[i] in freq_di):
            freq_di[di[i]] += 1
        else:
            freq_di[di[i]] = 1
    once = False
    for i in freq_di:
        if (i == 1 and freq_di[i] != 1):
            return "NO"
        if(freq_di[i] == 1 and once == True):
            return "NO"
        if(freq_di[i] == 1 and once == False):
            once = True
        
    return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
