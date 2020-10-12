import sys
from collections import deque

course = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())

for i in range(N):
    plan = sys.stdin.readline().rstrip()

    # 필수과목으로 만든 큐
    dq = deque(course)

    for c in plan:
        if c in dq:
            # 필수과목의 맨 앞이랑 다르면 틀린거
            if c != dq.popleft():
                print("#{} NO".format(i+1))
                break
                
    # 순서는 다 통과함
    else:
        # 남은 것도 없다면 통과
        if len(dq) == 0:
            print('#{} YES'.format(i+1))
        # 먼가 남아있으면 틀린거
        else:
            print('#{} NO'.format(i+1))
        