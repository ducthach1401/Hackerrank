from itertools import combinations_with_replacement

s, repeat = input().split()
s1 = []
for i in s:
    s1.append(i)
s1.sort()
s = ''.join(s1)
repeat = int(repeat)
for i in list(combinations_with_replacement(s, repeat)):
    print (''.join(i))
