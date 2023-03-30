import sys
input = sys.stdin.readline

def fib(n):
    dp = [i for i in range(n+1)]
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = int(input())
print(fib(n))