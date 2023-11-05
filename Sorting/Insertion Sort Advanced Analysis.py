#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def mergeSort(arr):
    count = 0

    def merge(arr, left, right, mid):
        nonlocal count
        left_half = arr[left:mid + 1]
        right_half = arr[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
                count += len(left_half) - i
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    def mergeSortHelper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            mergeSortHelper(arr, left, mid)
            mergeSortHelper(arr, mid + 1, right)
            merge(arr, left, right, mid)

    mergeSortHelper(arr, 0, len(arr) - 1)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = mergeSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
