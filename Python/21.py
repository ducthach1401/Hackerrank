A = list(map(int, input().split()))
num = int(input())
for i in range(num):
    temp = list(map(int, input().split()))
    for i in temp:
        if (i in A):
            kq = True
        else:
            kq = False
            break
    if (kq == False):
        break
print (kq)
