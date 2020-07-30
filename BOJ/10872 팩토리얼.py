"""
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

출력
첫째 줄에 N!을 출력한다.
"""
n = int(input())

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

print(factorial(n))

"""
factorial(5):

= 5*factorial(4)
= 5*4*factorial(3)
= 5*4*3*factorial(2)
= 5*4*3*2*factorial(1)
= 5*4*3*2*1*factorial(0)
= 5*4*3*2*1

"""

