#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    count = 0
    flag = False
    dig = 0
    low = 0
    up = 0
    sp_ch = 0
    for i in password:
        if (i in numbers):
            dig += 1
        if ( i in lower_case):
            low += 1
        if (i in upper_case):
            up += 1
        if (i in special_characters):
            sp_ch += 1
    while True:
        if (dig < 1):
            password += '1'
            dig += 1
        if (low < 1 ):
            password += 'a'
            low += 1
        if (up < 1 ):
            password += 'A'
            up += 1
        if (sp_ch < 1):
            password += '#'
            sp_ch += 1
        if (len(password) < 6):
            password += ("a" * (6 - len(password)))
        
        return len(password) - n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
