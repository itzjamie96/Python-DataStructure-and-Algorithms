# 두 성적이 한명보다 떨어지면 걍 뺌
import sys

T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())

    scores = []
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        scores.append((a, b))

    cnt = 1
    scores.sort()
    # print(scores)

    rank = scores[0][1]
    for i in range(1, N):
        if scores[i][1] < rank:
            cnt += 1
            rank = scores[i][1]


    print(cnt)

