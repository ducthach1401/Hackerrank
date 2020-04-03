if __name__ == '__main__':
    N = int(input())
    result = []
    for i in range(N):
        doing, *arr = input().split()
        arr = list(map(int, arr))
        if (doing == "insert"):
            result.insert(arr[0], arr[1])
        elif (doing == "print"):
            print (result)
        elif (doing == "remove"):
            result.remove(arr[0])
        elif (doing == "append"):
            result.append(arr[0])
        elif (doing == "sort"):
            result.sort()
        elif (doing == "pop"):
            result.pop()
        elif (doing == "reverse"):
            result.reverse()
