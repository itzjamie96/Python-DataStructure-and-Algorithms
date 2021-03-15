from collections import deque
N, M = map(int, input().split())
weights = list(map(int, input().split()))

weights = sorted(weights)
que = deque(weights)

result = 0
left = M - que.pop()
while que:
    if left >= list(que)[0]:
        left -= que.popleft()
    else:
        result += 1
        left = M - que.pop()

if left > 0:
    result += 1
print(result)




