'''
[이건 시간초과]
1부터니까 n이 0일 때 종료
global currSum을 두고
currSum에 현재 값 더하고 n-1호출하는 방식이면 될 듯?

[하나 뺀 숫자랑 더해보기]
n이 0이되면 종료
그게 아니면 n + f(n-1)

!!!!!!!!!아 그냥 최대 재귀 범위 벗어난거였다 ㅂㄷㅂㄷ...
import sys
sys.setrecursionlimit(1000000)
'''
import sys
sys.setrecursionlimit(1000000)

def getSum(n):
    if n <= 1:
        return n
    else:
        return n + getSum(n-1)

n = int(input())
print(getSum(n))
