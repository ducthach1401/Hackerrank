#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.


def migratoryBirds(arr):
    bird = {}
    max1 = 1
    for i in arr:
        if (i in bird) == 0:
            bird[i] = 1
        else:
            bird[i] += 1
            if (bird[i] > max1):
                max1 = bird[i]
                value = i
            elif (bird[i] == max1):
                if (i < value):
                    value = i
    return value


if __name__ == '__main__':
    fptr = open('text.txt', 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
