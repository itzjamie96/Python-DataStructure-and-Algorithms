"""
첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.

모든 막대를 놓은 격자판의 상태를 출력한다.
막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
단, 각 숫자는 공백으로 구분하여 출력한다.

<입력예시>
5 5       => 격자판 크기
3         => 막대 갯수
2 0 1 1   => 막대 길이, 가로/세로, 좌표
3 1 2 3
4 1 2 5

<출력예시>
1 1 0 0 0
0 0 1 0 1
0 0 1 0 1
0 0 1 0 1
0 0 0 0 1
"""

# 격자판
board = []

# 가로 세로
h,w = map(int, input().split())

# 막대 갯수
n = int(input())

# 막대들 담을 리스트
sticks = []

# 막대 갯수만큼 막대 정보 받기
for i in range(n):
    # 막대의 길이(l), 방향(d), 좌표(x, y)
    # 방향: 0 = 가로 / 1 = 세로
    l,d,x,y = map(int, input().split())

    # 딕셔너리로 만들어서 리스트에 추가
    info = {
        "len" : l,
        "dir" : d,
        "x" : x,
        "y" : y
        # x가 세로 y가 가로
    }
    sticks.append(info)


# 격자판 생성
row = []
for width in range(w):
    row.append(0)
for height in range(h):
    board.append(row[:])

# 각 막대 격자판에 추가하기
for stick in sticks:
    len = stick["len"]
    dir = stick["dir"]
    x = stick["x"] - 1  # 인덱스 값이랑 맞추기 위해 -1
    y = stick["y"] - 1

    # 만약 방향이 가로라면
    if dir == 0:
        # 가로 좌표 ~ 가로좌표 + 길이까지
        for i in range(y, len+y):
            # x번째 세로 줄의 가로 좌표값들을 1로 바꾼다
            board[x][i] = 1

    # 만약 방향이 세로라면
    else:
        # 세로 좌표 ~ 세로좌표 + 길이까지
        for i in range(x, len+x):
            board[i][y] = 1

# 격자판 프린트
for i in board:
    # 리스트 내용물을 " "로 연결해서 프린트하기
    print(" ".join(map(str, i)))




