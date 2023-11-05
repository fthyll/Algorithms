#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Initialize variables to store the sums of the two diagonals
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    n = len(arr)  # Get the number of rows or columns (assuming it's a square matrix)

    for i in range(n):
        # Sum the elements on the primary diagonal (top-left to bottom-right)
        primary_diagonal_sum += arr[i][i]

        # Sum the elements on the secondary diagonal (top-right to bottom-left)
        secondary_diagonal_sum += arr[i][n - 1 - i]

    # Calculate the absolute difference between the two diagonal sums
    diagonal_abs_diff = abs(primary_diagonal_sum - secondary_diagonal_sum)
    
    return diagonal_abs_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
