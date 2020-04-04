import numpy

n,m=map(int,input().strip().split())

print (str(numpy.eye(n,m,k=0)).replace('1',' 1').replace('0',' 0'))
