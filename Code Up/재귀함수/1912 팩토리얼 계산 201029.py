'''
n!을 구하는거는
n x n-1이잖아?
global value 설정하고
그거에 n-1을 곱해주자

+ value가 0이면 뭘 곱해도 0이다...^^...
'''
def factorial(n):
    global value
    if n == 0:
        return
    else:
        value *= n
        factorial(n-1)


n = int(input())
value = 1
factorial(n)
print(value)