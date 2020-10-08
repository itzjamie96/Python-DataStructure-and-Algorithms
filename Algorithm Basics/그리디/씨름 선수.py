'''
- or 조건이니까 둘다 아닌 애를 뽑으면 되는거 아닌가?
'''
import sys

N = int(sys.stdin.readline())
players = []

for _ in range(N):
    height, weight = map(int, sys.stdin.readline().split())
    players.append((height, weight))

# 키, 몸무게 둘 다 작은 사람 수를 세서 총 인원에서 다 안되는 애들 빼기
cnt = 0
for i in range(N):
    for j in range(1, N):
        if players[i][0] < players[j][0] and players[i][1] < players[j][1]:
            cnt += 1
            break

# print(cnt)
print(N - cnt)