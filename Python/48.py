na = int(input())
a = set(map(int, input().split()))
nb = int(input())
b = set(map(int, input().split()))
temp = a.difference(b)
temp.update(b.difference(a))
number = range(len(temp))
for i in number:
    print (min(temp))
    temp.discard(min(temp))
