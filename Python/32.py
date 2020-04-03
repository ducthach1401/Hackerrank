def print_rangoli(size):
    list_alpha = list(map(chr, range(97, 123)))
    temp = list_alpha[0:size]
    temp = temp[::-1]
    list_a = temp + list_alpha[1:size]
    width=len(list_a)+ len(list_a)-1
    for i in range(1, size + 1):
        temp = list_a[0:i - 1]
        temp = temp[::-1]
        printlist = list_a[0:i] + temp
        print('-'.join(printlist).center(width, '-'))
    for i in range(size - 1, 0, -1):
        temp = list_a[0:i - 1]
        temp = temp[::-1]
        printlist = list_a[0:i] + temp
        print('-'.join(printlist).center(width, '-'))


print_rangoli(5)
