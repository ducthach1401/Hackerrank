n = int(input())
for i in range(n):
    a, b = input().split()
    try:
        a = int(a)
        b = int(b)
        print (a // b)
    except ZeroDivisionError as e:
        print ('Error Code:', e)
    except ValueError as e:
        print ('Error Code:', e)
