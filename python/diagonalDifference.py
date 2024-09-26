#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

os.environ['OUTPUT_PATH'] = 'output.txt'

def diagonalDifference(arr):
    summ_diagonal = 0
    summ_diagonal_second = 0
    for i in range(len(arr)):
        summ_diagonal += arr[i][i]
    for i in range(len(arr)):
        summ_diagonal_second += arr[i][len(arr) - 1 - i]
    result = abs(summ_diagonal_second - summ_diagonal)
    print(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()