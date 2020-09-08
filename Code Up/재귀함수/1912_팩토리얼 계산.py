'''
팩토리얼~ 재귀로 해보아요
'''
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
print(factorial(n))