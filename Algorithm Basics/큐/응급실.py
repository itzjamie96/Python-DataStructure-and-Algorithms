'''
튜플로 받는다 (첫 입력 순서, 값) 
첫번째를 꺼내본다
값을 기준으로(1번째) 나머지 중 더 큰 수 가 있으면 뒤로 보내버린다
없으면:
    만약 0번째가 M이면 바로 print cnt
    아니면 cnt +1, 0번째 빼버림
    
'''

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline().split()))
patients = deque(list((i, value) for i, value in enumerate(tmp)))
# print(patients)

cnt = 0
while patients:

    current = patients[0]

    for i, p in patients:
        if p > current[1]:
            patients.popleft()
            patients.append(current)
            break
    else:
        if current[0] == M:
            print(cnt+1)
            break
        else:
            cnt += 1
            patients.popleft()

