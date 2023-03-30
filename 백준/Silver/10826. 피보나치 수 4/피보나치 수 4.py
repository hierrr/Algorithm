import sys
input = sys.stdin.readline

def fib(n):
    if not n:
        return 0
    c = 1
    p, pp = 1, 0
    for _ in range(n-1):
        c = pp + p
        p, pp = c, p
    return c

n = int(input())
print(fib(n))