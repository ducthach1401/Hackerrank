import numpy
line = input().split()
result = list(map(int, line))
result = numpy.array(result)
result.shape = (3, 3)
print (result)
