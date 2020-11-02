'''
방금 푼 합이같은거랑 비슷함
C = 기준무게
N = 바둑이 마리
visited = N개 리스트
max = 0
부분집합구하기
- 종료조건:
    현재합이 C보다 작고 현재 max보다 클때 max 갱신 후 종료
- 포함:
    visited[v] = 1
    f(현재합+바둑[v], idx+1)
- 미포함:
    visited = 0
    f(현재합, idx+1)
'''
def maxWeight(currSum, idx, tmpSum):
    global maxi
    
    # 현재 합 + 앞으로 남은 합이 지금 있는 maxi보다 작으면 볼 필요도 없다
    if currSum + (total - tmpSum) < maxi:
        return

    if currSum > C:
        return

    if idx == N:
        if maxi < currSum:
            maxi = currSum
        return
    else:
        # visited[idx] = 1
        maxWeight(currSum+dogs[idx], idx+1, tmpSum+dogs[idx])

        # visited[idx] = 0
        maxWeight(currSum, idx+1, tmpSum+dogs[idx])

C, N = map(int, input().split())
dogs = [int(input()) for _ in range(N)]
# visited = [0]*N
maxi = 0
total = sum(dogs)
maxWeight(0, 0, 0)
print(maxi)
# print(sum(dogs)-C)