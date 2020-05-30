#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    tim_head = 3
    value = 3
    old_tim_head = 0
    while True:
        if (t <= tim_head):
            return (value - (t - (old_tim_head + 1)))
        else:
            value *= 2
            old_tim_head = tim_head
            tim_head += value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
