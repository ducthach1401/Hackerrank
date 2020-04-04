import numpy
arr=[]
n,m=map(int,input().split())
for i in range(n):
	temp=list(map(int,input().split()))
	arr.append(temp)
arr=numpy.array(arr)
result=numpy.min(arr,axis=1)
print(numpy.max(result))