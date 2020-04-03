def split_and_join(line):
    s = line.split(' ')
    s1 = "-".join(s)
    return s1


print (split_and_join('this is a string'))
