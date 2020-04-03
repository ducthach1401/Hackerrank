from collections import defaultdict

n, m = map(int, input().split())
result = defaultdict(list)
for i in range(1, n + 1):
    temp = input()
    result[temp].append(i)
for i in range(m):
    temp = input()
    if (result[temp] == []):
        print (-1)
    else:
        print (' '.join(map(str, result[temp])))
