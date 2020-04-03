if __name__ == '__main__':
    k = int(input())
    arr = list(map(int, input().split()))
    duyet = []
    from collections import Counter
    counts = Counter(arr)
    for num, count in counts.items():
        if (count == 1):
            print (num)
