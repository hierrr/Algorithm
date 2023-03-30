import sys
input = sys.stdin.readline

def fib(n):
    if not n:
        return 0
    c = 1
    pp, p = 0, 1
    for _ in range(n-1):
        c = pp + p
        pp, p = p, c
    return c

n = int(input())
print(fib(n))