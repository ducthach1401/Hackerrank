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
    cheochinh = 0
    cheophu = 0
    for i in range(len(arr)):
        cheochinh += arr[i][i]
        cheophu += arr[i][len(arr) - 1 - i]
    return (abs(cheochinh - cheophu))


if __name__ == '__main__':
    fptr = open('text.txt', 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
