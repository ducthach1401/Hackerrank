#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    hour = s[0:2]
    minute = s[3:5]
    second = s[6:8]
    if ('PM' in s):
        if (hour != '12'):
            hour = str(int(hour) + 12)
    elif (hour == '12'):
        hour = '00'
    return (':'.join([hour, minute, second]))


if __name__ == '__main__':
    f = open('text.txt', 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
