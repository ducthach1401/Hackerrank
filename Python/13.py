import numpy
n, m = input().split()
n = int(n)
m = int(m)
result = list()
for i in range(n):
    line = input().split()
    temp = list(map(int, line))
    result.append(temp)
result = numpy.array(result)
print (result.transpose())
print (result.flatten())
