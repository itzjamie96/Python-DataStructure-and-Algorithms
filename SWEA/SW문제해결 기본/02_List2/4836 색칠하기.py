'''
1. 먼저 10*10 보드판 생성
2. p1(왼쪽위), p2(오른쪽아래) 좌표 값 받기
    - 가로: p1[0] ~ p2[0]
    - 세로: p1[0] ~ p2[1]
3. 가로 세로 가지고 for문으로 색칠할 값을 "더해주기"
4. 겹치는 부분 = 빨강+파랑 = 3
5. 보드판에서 겹치는 영역 카운팅하기

'''
import sys

T = int(sys.stdin.readline())
for tc in range(1, T+1):

    # 보드판 입력받기 (0 ~ 9까지)
    board = [[0]*10 for _ in range(10)]
    
    # 색칠 몇개 할건지 입력받기
    N = int(sys.stdin.readline())
    for i in range(N):
        
        # 색칠할 영역 정보를 먼저 리스트로 받는다
        tmp = list(map(int, sys.stdin.readline().split()))
        p1 = (tmp[0], tmp[1])   #왼쪽 위 좌표
        p2 = (tmp[2], tmp[3])   #오른쪽 아래 좌표
        color = tmp[4]          #색칠할 색상 값

        # p2[0]을 포함한 영역까지 칠해야하니 +1
        for row in range(p1[0], p2[0]+1):
            for col in range(p1[1], p2[1]+1):
                # 보드의 해당 위치에 색상으로 더!해!줌 (대체 ㄴㄴ)
                board[row][col] += color

    cnt = 0     # 겹치는 영역을 셀 변수 cnt

    # 보드판을 돌면서 값이 3인 부분이 있으면 cnt+1
    for row in range(10):
        for col in range(10):
            if board[row][col] == 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))