def DFS(idx, currentSum):

    global maxi
    
    if currentSum > C:  #C보다 현재합이 더 크면 그냥 지금껀 종료
        return 

    if idx == N:        # 종료지점에 왔을 때 현재합이랑 최대랑 비교후 스왑
        if currentSum > maxi:
            maxi = currentSum

    else:
        DFS(idx+1, currentSum + dogs[idx])
        DFS(idx+1, currentSum)

C, N = map(int, input().split())
dogs = [0]*N
for i in range(N):
    dogs[i] = int(input())

maxi = 0
DFS(0, 0)
print(maxi)