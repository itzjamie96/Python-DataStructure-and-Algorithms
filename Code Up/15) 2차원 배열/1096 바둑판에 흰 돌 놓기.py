# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
# n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

# 바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력된다.
# 둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x, y)가 n줄 입력된다.
# n은 10이하의 자연수이고 x, y 좌표는 1 ~ 19 까지이며, 같은 좌표는 입력되지 않는다.
# 흰 돌이 올려진 바둑판의 상황을 출력한다.
# 흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력한다.

# 흰 돌의 개수
n = int(input())

# 흰 돌 좌표값 받기
dol = []
for i in range(n):
    dol.append(list(map(int, input().split())))

# 바둑판 생성
board = []

# 19개의 0을 가진 리스트 생성
row = []
for i in range(19):
    row.append(0)

# 파이썬에서 리스트 복사 방법 1: slice 전체 = 복사 후 신규 생성
for i in range(19):
    board.append(row[:])

# 각 돌의 좌표에서
for d in dol:

    # row, column 값 추출 후 -1 (인덱스번호는 하나 작음)
    row = d[1]-1
    col = d[0]-1

    # 해당 좌표값은 1로 바꿔주기
    board[col][row] = 1

# 바둑판 프린트!
for i in range(len(board)):
    row = board[i]
    for j in row:
        print(j, end=" ")
    print()