from itertools import groupby

s = input()
count = {}
result = []
temp = s[0]
for i in s:
    if (i in count) == False:
        count[i] = 1
    else:
        count[i] = count[i] + 1
    result.append([i, count[i]])
for i, j in result:
    print (i, j)
print (' '.join(map(str, result)))
