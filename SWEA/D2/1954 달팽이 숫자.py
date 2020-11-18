'''
방향: right, down, left, up
- N * N의 배열을 만든다
- 반복문: 1 ~ N*N까지
    - 현재 x, y가 유효하면 print(i)
    - 안 유효하면 방향%4로 틀기
'''
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    snail = [[0]*N for _ in range(N)]

    x, y = 0, 0
    i = 2
    d = 0
    snail[x][y] = 1
    while i <= N*N:

        if -1<x+dx[d%4]<N and -1<y+dy[d%4]<N and snail[x+dx[d%4]][y+dy[d%4]] == 0:
            x = x+dx[d%4]
            y = y+dy[d%4]
            snail[x][y] = i
            i += 1
        else:
            d += 1
    print('#{}'.format(tc))
    for i in range(N):
        print(*snail[i])

