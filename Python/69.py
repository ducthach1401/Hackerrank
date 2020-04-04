import numpy

n,m = map(int,input().split())
A=0
B=0

temp=[]
for i in range(n):
	A=list(map(int,input().split()))
	temp.append(A)
A=numpy.array(temp,int)

temp=[]
for i in range(n):
	B=list(map(int,input().split()))
	temp.append(B)
B=numpy.array(temp,int)
print (numpy.add(A,B))
print (numpy.subtract(A,B))
print (numpy.multiply(A,B))
print (numpy.divmod(A,B)[0])
print (numpy.mod(A,B))
print (numpy.power(A,B))