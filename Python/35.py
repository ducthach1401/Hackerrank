def merge_the_tools(string, k):
    process = []
    div = len(string) // k
    dem = 0
    temp = ''
    for i in string:
        dem = dem + 1
        temp = temp + i
        if dem == k:
            process.append(temp)
            dem = 0
            temp = ''
    for i in process:
        temp1 = []
        for j in i:
            if (j in temp1) == False:
                temp1.append(j)
        print (''.join(temp1))


of = open('test.txt', 'r')
string = of.read()
string, k = string.split('\n')
of.close()
k = int(k)
merge_the_tools(string, k)
