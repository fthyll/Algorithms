#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    count = [0] * 20001
    max = 0
    for i in arr:
        count[i] += 1
        if i > max:
            max = i
    result = []
    for i in range(max+1):
        result += [i] * count[i]
    return result[len(result)//2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
