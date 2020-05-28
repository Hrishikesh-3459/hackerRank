#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    row = len(grid)
    col = len(grid[0])
    if (row == 2 and col == 2):
        return grid
    
    ans = []
    for i in range(row):
        x = ""
        for j in range(col):
            if (i != 0 and i != row -1 and j != 0 and j != col-1):
                cur = int(grid[i][j])
                if (cur > int(grid[i-1][j]) and
                    cur > int(grid[i+1][j]) and 
                    cur > int(grid[i][j-1]) and 
                    cur > int(grid[i][j+1])):
                    x += "X"
                else:
                    x += (grid[i][j])
            else:
                x += (grid[i][j])
        ans.append(x)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
