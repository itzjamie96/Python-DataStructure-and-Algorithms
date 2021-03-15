# 지원자의 수
N = int(input())

# N명의 키와 몸무게
physical = []
for _ in range(N):
    h, w = map(int, input().split())
    physical.append((h, w))

physical = sorted(physical, reverse=True)

result = 0
heavy = 0
for h, w in physical:
    if w >= heavy:
        result += 1
        heavy = w

print(result)
