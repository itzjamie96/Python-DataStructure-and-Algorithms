import sys

N = int(sys.stdin.readline())       # 낸 돈
coins = [500, 100, 50, 10, 5, 1]    # 거슬러줄 수 있는 동전들
amount = 1000 - N                   # 거슬러줘야 할 돈

cnt = 0     # 거스름돈 동전의 갯수

for coin in coins:
    
    # 만약 현재 동전으로만 다 거슬러 줄 수 있으면 그렇게 해준다
    if amount % coin == 0:
        cnt += amount // coin
        break

    # 그게 아니라면 우선 현재 동전으로 최대한 많이 거슬러 주고 다음 동전으로 가능한지 넘긴다
    else:
        cnt += amount // coin
        amount = amount % coin

        if amount == 0: #만약 남은돈이 0이 됐으면 끝낸다
            break

print(cnt)