from collections import Counter

if __name__ == '__main__':
    n = int(input())
    numbershoe = list(map(int, input().split()))
    customer = int(input())
    result = 0
    temp = Counter(numbershoe)
    for i in range(customer):
        size, cost = map(int, input().split())
        if (temp[size] > 0):
            result = result + cost
            temp[size] = temp[size] - 1
    print (result)
