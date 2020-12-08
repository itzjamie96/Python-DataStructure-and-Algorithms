def getSubset(n):
    if n > N:
        for i in range(N+1):
            if visited[i] == 1:
                print(i, end=' ')
        print()
    else:
        visited[n] = 1
        getSubset(n+1)
        visited[n] = 0
        getSubset(n+1)

N = int(input())
visited = [0]*(N+1)
getSubset(1)