#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Write your code here
    count = 0
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > temp:
                arr[j+1] = arr[j]
                count += 1
            else:
                arr[j+1] = temp
                break
        if arr[0] > temp:
            arr[0] = temp
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
