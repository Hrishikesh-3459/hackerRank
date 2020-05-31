#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    opp = {')': '(', ']': '[', '}': '{'}
    stack = []
    for i in s:
        if stack and i in opp:
            if (stack[-1] == opp[i]):
                stack.pop()
            else:
                return "NO"
        else:
            stack.append(i)
    if (stack):
        return "NO"
    return "YES"
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
