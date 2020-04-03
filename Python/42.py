from itertools import combinations

s, repeat = input().split()
s1 = []
for i in s:
    s1.append(i)
s1.sort()
s = ''.join(s1)
repeat = int(repeat)
for k in range(1, repeat + 1):
    for i in list(combinations(s, k)):
        print (''.join(i))
