def solve(s):
    s = s.capitalize()
    kt = False
    for i in range(len(s)):
        if (s[i] == " "):
            kt = True
        else:
            if (kt):
                s = s[:i] + s[i:].capitalize()
            kt = False
    return s


s = "chris alan  12  alo"
print (solve(s))
