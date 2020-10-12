import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

DQ = list(range(1, N+1))
DQ = deque(DQ)

while DQ:

    for _ in range(K-1):
        current = DQ.popleft()
        DQ.append(current)

    DQ.popleft()

    if len(DQ) == 1:
        print(DQ[0])
        DQ.popleft()    #break 대신 길이가 0이 되어 while문 끝남