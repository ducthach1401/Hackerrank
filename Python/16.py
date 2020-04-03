import math
import os
import random
import re
import sys


def stringSimilarity(s):
    result = int(len(s))
    s1 = s
    while len(s) != 0:
        s = s[1:]
        for i in range(len(s)):
            if s[i] == s1[i]:
                result = result + 1
            else:
                break
    return result


if __name__ == '__main__':
    fptr = open('text.txt', 'w')
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = stringSimilarity(s)
        fptr.write(str(result) + '\n')
    fptr.close()
