#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
	arr=[]
	result=0
	for i in range(1,102):
		arr.append(0)
	for i in ar:
		arr[i]+=1
		if (arr[i]%2==0):
			result+=1
	return result
if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)