import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

# enumerate로 한방에 받는 방법
patients = [(idx, value) for idx, value in enumerate(list(map(int, sys.stdin.readline().split())))]
patients = deque(patients)

cnt = 0

while True:
    current = patients.popleft()
    
    # any: 알아서 for문 돌려서 하나라도 조건에 맞는게 있는지 확인
    # patients의 x에 대해서 x[1]이 current[1]보다 큰게 있는지 확인
    # 만족하는 조건이 하나라도 있으면 바로 True
    if any(current[1] < x[1] for x in patients):
        patients.append(current)
    else:
        cnt += 1
        if current[0] == M:
            print(cnt)
            break