#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
	sea=0
	thunglung=False
	result=0
	for i in s:
		if (i=='U'):
			sea+=1
		else:
			sea-=1
		if (sea<0):
			thunglung=True
		if (thunglung) and (sea==0):
			result+=1
			thunglung=False
	return result

if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print (result)
