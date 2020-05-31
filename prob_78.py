#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    q = ['h','a','c','k','e','r','r','a','n','k']
    for i in s:
        if (i == q[0]):
            q.pop(0)
        if (len(q) == 0):
            return("YES")
    
    return("NO")
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
