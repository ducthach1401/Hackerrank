def average(array):
    sum1, n = 0, 0
    for i in set(array):
        sum1 = sum1 + i
        n = n + 1
    return (sum1 / n)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print (result)
