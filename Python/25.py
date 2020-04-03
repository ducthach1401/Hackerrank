def swap_case(s):
    s1 = ''
    for i in s:
        if i.isupper():
            s1 = s1 + i.lower()
        else:
            s1 = s1 + i.upper()
    return s1


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print (result)
