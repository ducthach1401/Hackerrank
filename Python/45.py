from cmath import phase

n = input()
flag = False
for i in range(len(n)):
    if ((n[i] == '+') or (n[i] == '-')) and (i != 0):
        one = int(n[0:i])
        flag = True
        vt = i
    if (flag) and (n[i] == 'j'):
        two = int(n[vt:i])
print (abs(complex(one, two)))
print (phase(complex(one, two)))
