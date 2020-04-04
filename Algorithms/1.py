import math
import os
import random
import re
import sys

def bonAppetit(bill,k,b):
	result=0
	for i in range(len(bill)):
		if (i!=k):
			result+=bill[i]
	result/=2
	if (result==b):
		print ("Bon Appetit")
	else:
		print(int(b-result))
if __name__=='__main__':
	nk = input().rstrip().split()
	n = int(nk[0])
	k = int(nk[1])
	bill = list(map(int, input().rstrip().split()))
	b = int(input().strip())
	bonAppetit(bill, k, b)