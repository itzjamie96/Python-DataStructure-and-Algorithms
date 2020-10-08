'''
- 키/몸무게 둘 중 하나를 기준으로 정렬해서 풀기
'''

import sys

N = int(sys.stdin.readline())
players = []
for _ in range(N):
    h, w = map(int, sys.stdin.readline().split())
    players.append((h, w))

# 한가지 기준으로 정렬 (키로 내림차순)
players.sort(reverse=True)

# 몸무게 최대
maxi = 0
cnt = 0

for h, w in players:
    if w>maxi:
        maxi = w
        cnt += 1

print(cnt)