'''

'''
def DFS(v):
    global cnt
    if v == N:
        cnt += 1
        print(*path)
    else:
        for i in range(1, N+1):
            # 갈 수 있고 방문한 적 없으면
            if graph[v][i] == 1 and check[i] == 0:
                check[i] = 1
                path.append(i)
                DFS(i)  #방문하러 간다

                #방문 후
                check[i] = 0
                path.pop()


N, M = map(int, input().split())

# 1~N까지니까 N+1까지 돌린다
graph = [[0]*(N+1) for _ in range(N+1)]

check = [0]*(N+1)

# 그래프 연결노드 보기
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

cnt = 0

# 경로 저장용
path = []
path.append(1)

check[1] = 1    #1번 노드 방문했다
DFS(1)

print(cnt)