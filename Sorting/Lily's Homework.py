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
    def min_swaps_to_sort(arr):
        sorted_arr = sorted(arr)
        index_map = {value: index for index, value in enumerate(arr)}
        swaps = 0

        for i in range(len(arr)):
            if arr[i] != sorted_arr[i]:
                swaps += 1
                correct_value = sorted_arr[i]
                current_value = arr[i]
                correct_index = index_map[correct_value]
                arr[i], arr[correct_index] = arr[correct_index], arr[i]
                index_map[current_value] = correct_index
                index_map[correct_value] = i

        return swaps

    ascending_swaps = min_swaps_to_sort(arr.copy())
    descending_swaps = min_swaps_to_sort(arr[::-1])

    return min(ascending_swaps, descending_swaps)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
