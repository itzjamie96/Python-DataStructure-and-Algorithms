def getSubset(idx, currSum):
    if idx > N:
        for i in range(N+1):
            if visited[i] == 1:
                pass

N = int(input())
arr = list(map(int, input().split()))
visited = [0] * (N+1)