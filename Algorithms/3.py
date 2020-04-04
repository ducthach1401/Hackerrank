#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
	if (n+1)%2==0:
		trang=n+1
	else:
		trang=n+2
	if (p%2==0):
		stt=p+2
	else:
		stt=p+1
	stt1=stt/2-1
	stt2=trang/2-stt1-1
	return min(int(stt1),int(stt2))
if __name__ == '__main__':
    n = int(input())

    p = int(input())

    result = pageCount(n, p)
    print (result)