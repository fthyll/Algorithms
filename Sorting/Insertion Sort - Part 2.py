#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        temp = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > temp:
                arr[j+1] = arr[j]
            else:
                arr[j+1] = temp
                break
        if arr[0] > temp:
            arr[0] = temp
        print(*arr)
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
