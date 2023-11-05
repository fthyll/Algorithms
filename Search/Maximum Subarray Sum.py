#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

def maximumSum(a, m):
    n = len(a)
    prefix_sum = [0] * n
    prefix_sum_mod = [0] * n
    prefix_sum[0] = a[0]
    prefix_sum_mod[0] = a[0] % m
    max_sum_mod = prefix_sum_mod[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + a[i]
        prefix_sum_mod[i] = prefix_sum[i] % m

        max_sum_mod = max(max_sum_mod, prefix_sum_mod[i])

    # Find the maximum difference between two prefix sums with the same modulo
    sorted_mods = sorted(enumerate(prefix_sum_mod), key=lambda x: x[1])
    max_difference = 0

    for i in range(n - 1):
        if sorted_mods[i][0] > sorted_mods[i + 1][0]:
            max_difference = max(max_difference, (sorted_mods[i][1] - sorted_mods[i + 1][1] + m) % m)

    return max(max_sum_mod, max_difference)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()

