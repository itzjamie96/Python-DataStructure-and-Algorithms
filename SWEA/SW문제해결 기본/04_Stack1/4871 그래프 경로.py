'''
모든 경로의 경우를 path 라는 리스트에 담아둠
path에 V,E가 둘 다 있으면 1, 없으면 0
'''
def DFS(vertex):
    global ans
    if vertex == G:
        if G in path:
            ans = 1
            # print(*path)

    else:
        for i in range(1, V+1):
            if graph[vertex][i] == 1 and visited[i] == 0:
                visited[i] = 1
                path.append(i)
                DFS(i)
                visited[i] = 0
                path.pop()
                # print(*path)

T = int(input())
for tc in range(1, T+1):

    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)

    for i in range(E):
        a, b = map(int, input().split())
        graph[a][b] = 1

    S, G = map(int, input().split())
    # print('S:{}, G:{}'.format(S, G))
    # 경로 넣을 path
    path = []
    path.append(S)

    ans = 0
    visited[S] = 1
    DFS(S)

    print('#{} {}'.format(tc,ans))
