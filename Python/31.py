def print_formatted(number):
    s = len(bin(number)[2:])
    for i in range(1, number + 1):
        s1 = str(i).rjust(s)
        s2 = oct(i)
        s2 = s2[2:].rjust(s)
        s3 = hex(i)[2:].upper().rjust(s)
        s4 = bin(i)[2:].rjust(s)
        print (s1, s2, s3, s4)


n = 17
print_formatted(n)
