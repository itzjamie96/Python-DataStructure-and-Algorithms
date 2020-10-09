'''
(사람, 시간) => 시간 순으로 정렬
'''
import sys

N = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))

# 기억하기! enumerate
time = list(enumerate(tmp))
# print(time)

# 튜플의 1번째를 기준으로 정렬하기
time.sort(key=lambda x:(x[1], x[0]))
# print(time)

total = []

# 이게 왜 안되는 거지....몽총쓰...
for a, b in time:
    if len(total) == 0:
        total.append(b)
    else:
        total.append(total[-1]+b)


print(sum(total))
