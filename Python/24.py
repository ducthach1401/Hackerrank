if __name__ == '__main__':
    s = input()
    isalnum = False
    isalpha = False
    isNum = False
    isLower = False
    isUpper = False
    for i in range(len(s)):
        if (isalnum == False):
            isalnum = s[i].isalnum()
        if (isalpha == False):
            isalpha = s[i].isalpha()
        if (isNum == False):
            isNum = s[i].isdigit()
        if (isLower == False):
            isLower = s[i].islower()
        if (isUpper == False):
            isUpper = s[i].isupper()
    print (isalnum)
    print (isalpha)
    print (isNum)
    print (isLower)
    print (isUpper)
