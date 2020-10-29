'''
a, b 사이의 홀수
a(=작은수)부터 출력
- 종료 조건: a가 b보다 클 때
- 그 전까지 홀수면 프린트
- 이후 +2 호출
'''
def printOdd(a, b):
    if a > b:
        return
    else:
        if a%2:
            print(a, end=' ')
            printOdd(a+2, b)
        else:
            printOdd(a+1, b)

a, b = map(int, input().split())
printOdd(a, b)