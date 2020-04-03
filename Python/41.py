from itertools import permutations

s, repeat = input().split()
s1 = []
for i in s:
    s1.append(i)
s1.sort()
s = ''.join(s1)
repeat = int(repeat)
for i in list(permutations(s, repeat)):
    print (''.join(i))
