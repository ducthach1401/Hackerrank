n, m = int(input()), list(map(int, input().split()))
print (all([i > 0 for i in m]) and any(str(i)[::-1] == str(i) for i in m))
