'''
- 동전 리스트 받기 (N=길이)
- 동전 리스트의 길이랑 똑같은 리스트 만들기(visited)
- 중복순열 구하기

'''
def countCoins(level, totalMoney):
    global cnt
    if level > cnt:
        return
    if totalMoney > M:
        return
    if totalMoney == M:
        if level < cnt:
            cnt = level
    else:
        for i in range(N):
            countCoins(level + 1, totalMoney + coins[i])


N = int(input())
coins = list(map(int, input().split()))
M = int(input())
coins.sort(reverse=True)
cnt = 2147000000
countCoins(0, 0)
print(cnt)