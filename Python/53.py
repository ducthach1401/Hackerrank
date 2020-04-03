def sortd(x):
    temp = x
    temp.sort()
    return ''.join(temp)


my_string = input()
lower = []
upper = []
odd = []
even = []
for i in my_string:
    if (i.islower()):
        lower.append(i)
    elif (i.isupper()):
        upper.append(i)
    elif (i.isalnum()):
        if (int(i) % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
lower = sortd(lower)
upper = sortd(upper)
odd = sortd(odd)
even = sortd(even)
print (lower + upper + odd + even)
