import numpy

arr=list(map(float,input().split()))
numpy.set_printoptions(sign=' ')
num=numpy.array(arr)
print(numpy.floor(num))
print(numpy.ceil(num))
print(numpy.rint(num))