#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

def gridlandMetro(n, m, k, track):
    track_dict = {}

    # Populate the track dictionary with track information
    for row, start, end in track:
        if row not in track_dict:
            track_dict[row] = []
        track_list = track_dict[row]

        # Merge overlapping or adjacent track segments
        new_segment = [start, end]
        merged = False
        for i, (s, e) in enumerate(track_list):
            if start <= e and end >= s:
                new_segment = [min(start, s), max(end, e)]
                track_list[i] = new_segment
                merged = True
                break

        if not merged:
            track_list.append(new_segment)

    # Calculate the total cells covered by tracks in each row
    total_covered = 0
    for row, segments in track_dict.items():
        for s, e in segments:
            total_covered += e - s + 1

    # Calculate the total uncovered cells
    total_uncovered = n * m - total_covered

    return total_uncovered
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
