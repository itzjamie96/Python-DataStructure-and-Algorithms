'''
중복순열에서 앞의 [i]랑 다른 값만 넣기
'''
def getCoins(current):
    global cnt
    if current == M:
        print(*result, sep=' ')
        cnt += 1

    else:
        for i in range(1, N+1):
            if visited[i] == 0:
                visited[i] = 1
                result[current] = i
                getCoins(current+1)
                visited[i] = 0

N, M = map(int, input().split())
result = [0] * M
visited = [0]*(N+1)
cnt = 0
getCoins(0)
print(cnt)