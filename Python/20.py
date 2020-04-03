for i in range(int(input())):
    numA = int(input())
    A = list(map(int, input().split()))
    numB = int(input())
    B = list(map(int, input().split()))
    for i in A:
        if (i in B):
            kq = True
        else:
            kq = False
            break
    print (kq)
