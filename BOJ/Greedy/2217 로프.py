import sys

N = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline()) for _ in range(N)]

# 로프들을 작은 것 부터 큰 것 순서로 정렬한다
ropes.sort()

# 총 N개의 로프 중 현재 로프(=i)를 N-i개 중에서 제일 작은 로프라고 쳤을 때
# 그때 가능한 최대 중량이 keep된 최대보다 크면 갱신
maxi = 0
for i in range(len(ropes)):
    if ropes[i]*(N-i) > maxi:
        maxi = ropes[i]*(N-i)

print(maxi)