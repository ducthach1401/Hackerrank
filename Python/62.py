#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.


def kangaroo(x1, v1, x2, v2):
    try:
        k = (x2 - x1) / (v1 - v2)
        if (int(k) - k) != 0:
            return 'NO'
        elif (k < 0):
            return 'NO'
        else:
            return 'YES'
    except ZeroDivisionError:
        return 'NO'


if __name__ == '__main__':
    fptr = open('text.txt', 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
