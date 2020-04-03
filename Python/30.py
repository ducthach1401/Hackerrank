n, m = map(int, input().split())
SIGN = '.|.'
TEXT = 'WELCOME'
for i in range(n // 2):
    print((SIGN * (2 * i + 1)).center(m, '-'))
print(TEXT.center(m, '-'))
for i in range(1, n // 2 + 1):
    print((SIGN * (n - 2 * i)).center(m, '-'))
