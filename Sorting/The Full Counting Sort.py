#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    idxArr = [[] for i in range(100)]
    for i in range(len(arr)):
        idx = int(arr[i][0])
        if i < len(arr) / 2:
            idxArr[idx].append("-")
        else:
            idxArr[idx].append(arr[i][1])
    print(" ".join(map(lambda r: " ".join(r), idxArr)).lstrip().rstrip())

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
