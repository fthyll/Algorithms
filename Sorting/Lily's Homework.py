#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    reverse_sorted_arr = sorted(arr, reverse=True)
    count = 0
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            count += 1
    reverse_count = 0
    for i in range(len(arr)):
        if arr[i] != reverse_sorted_arr[i]:
            reverse_count += 1
    return min(count, reverse_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
