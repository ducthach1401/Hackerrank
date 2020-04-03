import re
n = int(input())
str = '123456789'
for i in range(n):
    my_str = input()
    try:
        re.findall(my_str, str)
    except re.error as e:
        print (False)
    else:
        print (True)
