#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
	result=0
	for i in range(len(s)-m+1):
		t=s[i:i+m]
		temp=sum(t)
		if (temp==d):
			result+=1
	return result
if __name__ == '__main__':
    fptr = open('text.txt', 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
