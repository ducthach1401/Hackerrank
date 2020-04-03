from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    ave = 0
    list_label = list(input().split())
    result = namedtuple('result', list_label)
    for i in range(n):
        list_ID = list(input().split())
        temp = result(list_ID[0], list_ID[1], list_ID[2], list_ID[3])
        ave = ave + int(temp.MARKS)
    ave = ave / n
    print (format(ave, '.2f'))
