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
row = []
for i in range(19):
    row.append(0)

# 파이썬에서 리스트 복사 방법 1: slice 전체
for i in range(19):
    board.append(row[:])

# 각 돌의 좌표값과 일치하는 판의 인덱스는 1로 값 변경
for d in dol:
    row = d[1]-1
    col = d[0]-1
    board[col][row] = 1

for i in range(len(board)):
    row = board[i]
    for j in row:
        print(j, end=" ")
    print()