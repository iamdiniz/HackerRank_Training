#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
os.environ['OUTPUT_PATH'] = 'output.txt'

def compareTriplets(a, b):
    point_a = 0
    point_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            point_a += 1
        elif b[i] > a[i]:
            point_b += 1
    print(f"{point_a} {point_b}")
    return point_a, point_b
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()