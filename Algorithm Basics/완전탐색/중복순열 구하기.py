'''
구슬 1~N 중 M개씩 뽑기
3 2

visited = [0,0]
visited[0]에 1~3
visited[1]에 1~3
- V가 2(M)이면 종료
'''
def perm(V):
    global cnt

    if V == M:
        for i in range(M):
            print(visited[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, N+1):
            visited[V] = i
            # print('V: {}, i:{}, visited:{}'.format(V, i, visited))
            perm(V+1)

import sys

N, M = map(int, sys.stdin.readline().split())
visited = [0]*(M)
cnt = 0

perm(0)
print(cnt)