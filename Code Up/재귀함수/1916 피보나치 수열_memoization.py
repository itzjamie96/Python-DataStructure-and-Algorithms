# import sys
# sys.setrecursionlimit(1000000)

memo = {}

def fibo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    if n not in memo:
        memo[n] = fibo(n-2) + fibo(n-1)
    return memo[n]

n = int(input())
print(fibo(n)%10009)
# print(memo)

