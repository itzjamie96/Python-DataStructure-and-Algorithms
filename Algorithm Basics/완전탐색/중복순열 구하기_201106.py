'''
1 ~ N까지
M개 뽑기
visited = M개 (ex. M=2 -> [0,0])

current = 0일 때
visited[current] = 1    [1, 0]

current = 1일 때
visited[current] = 1    [1, 1]

current = 2일 때 = M
[1, 1] 프린트
카운트 추가

'''
def countCoins(current):
    global cnt
    if current == M:
        for i in visited:
            print(i, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, N+1):
            visited[current] = i
            countCoins(current+1)

N, M = map(int, input().split())
visited = [0]*M
cnt = 0
countCoins(0)
print(cnt)
