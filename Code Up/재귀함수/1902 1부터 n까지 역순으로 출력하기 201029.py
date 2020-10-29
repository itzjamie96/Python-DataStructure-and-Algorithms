'''
input 값부터 나와야함 = 프린트 먼저 실행 후 함수 호출
n이 0일 때 리턴하면 1까지 프린트되고 종료됨
'''
def recurBackwards(n):
    if n == 0:
        return
    print(n)
    recurBackwards(n-1)

n = int(input())
recurBackwards(n)