# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

N = int(input())

def fibonacci(n):
    return fibonacci(n-1) + fibonacci(n-2) if n >= 2 else n

print(fibonacci(N))