import numpy

list1=[]
n,m=map(int,input().split())
for i in range(n):
	temp=list(map(int,input().split()))
	list1.append(temp)
arr=numpy.array(list1)
sum_arr=numpy.sum(arr,axis=0)
result=1
for i in sum_arr:
	result*=i
print(result)
