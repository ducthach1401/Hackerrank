from collections import OrderedDict

n = int(input())
list_item = OrderedDict()
for i in range(n):
    temp = list(input().split())
    item = ' '.join(temp[0:len(temp) - 1])
    value = int(temp[len(temp) - 1])
    if (item in list_item):
        list_item[item] = list_item[item] + value
    else:
        list_item[item] = value
    # list_item[]
for i in list_item:
    print (i, list_item[i])
