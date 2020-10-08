import sys

N, M = map(int, sys.stdin.readline().split())
weights = list(map(int, sys.stdin.readline().split()))

weights.sort()

cnt = 0

while weights:
    
    # 한 명 남았을 때는 그냥 cnt, break
    if len(weights) == 1:
        cnt += 1
        break

    if weights[0] + weights[-1] > M:
        weights.pop()   #무거운 애는 혼자 타고 가라
        cnt += 1
    else:
        weights.pop(0)
        weights.pop()
        cnt += 1

print(cnt)

