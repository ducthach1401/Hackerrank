import calendar
MM, DD, YY = map(int, input().split())
temp = calendar.weekday(YY, MM, DD)
tong = -1
temp1 = str(calendar.weekheader(9))
temp1 = temp1.split()
print (temp1[temp].upper())
