#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
	arr.sort()
	minarr=arr[0:4]
	maxarr=arr[1:5]
	print(sum(minarr),sum(maxarr))
if __name__ == '__main__':
	arr = list(map(int, input().rstrip().split()))
	miniMaxSum(arr)