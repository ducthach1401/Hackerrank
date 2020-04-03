if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if (_ == 0):
            students = list()
        students.append([name, score])

    def myfunc(e):
        return (e[1])
    students.sort(key=myfunc)
    minx = students[0][1]
    temp = list()
    for i in students:
        if (minx != i[1]):
            temp.append(i)
    minx = temp[0][1]
    result = list()
    for i in students:
        if (minx == i[1]):
            result.append(i[0])
    result.sort()
    for i in result:
        print (i)
