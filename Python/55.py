#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    mauso = len(arr)
    tru = 0
    cong = 0
    zero = 0
    for i in arr:
        if (i < 0):
            tru += 1
        elif (i > 0):
            cong += 1
        else:
            zero += 1
    print(format(cong / mauso, '.6f'))
    print(format(tru / mauso, '.6f'))
    print(format(zero / mauso, '.6f'))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
