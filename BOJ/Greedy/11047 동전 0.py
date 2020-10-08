import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]

cnt = 0
idx = N-1   #맨 마지막 인덱스부터 하나씩 내려올거다

# 0이 될때까지 뒤에서부터 내려옴
while idx >= 0:

    if K == 0:  #K가 0원이 되면 당연히 break
        break

    if coins[idx] <= K:         #K보다 작은 돈 단위가 나왔을 때
        cnt += K//coins[idx]    #우선 그 동전이 몇개 필요한지 카운팅하고
        K = K%coins[idx]        #남은 돈은 다시 K에 넣어줌
    
    #K보다 작은 단위를 찾았던 안찾았던 인덱스는 줄어든다
    idx -= 1

print(cnt)