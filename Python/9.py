if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    max1 = max(arr)
    temp = arr.count(max1)
    for i in range(temp):
        arr.remove(max1)
    max1 = max(arr)
    print (max1)
