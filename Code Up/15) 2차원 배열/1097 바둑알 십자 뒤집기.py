# 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
# n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

# 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
# 십자 뒤집기 횟수(n)가 입력된다.
# 십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.

# 바둑판 입력받기
board = []

# 각 row를 list로 받은 후 board에 넣어준다
for i in range(19):
    board.append(list(map(int, input().split())))

# 좌표(라기보단 행,렬)을 입력받을 횟수
n = int(input())

# 각 좌표를 넣어줄 리스트
nums = []

# nums에 각 좌표를 list로 받아서 넣어준다
for i in range(n):
    nums.append(list(map(int, input().split())))


# 각 좌표에 대해
for i in range(n):

    # row랑 column 값 추출
    # 인덱스 번호는 0부터 시작하니까 -1 해주기
    row = nums[i][0] -1
    col = nums[i][1] -1

    # 각 좌표값을 바꿔줄 때, 조건문을 쓸 수도 있지만 1에서 각 값을 빼주는게 더 빠를 듯
    # for문에서 일일이 if로 조건을 확인하면 엄청 느려지겠지?
    # 1-0=1, / 1-1=0 --> 각자 반대값이 나온다!

    # 바둑판에서 해당 row 한줄의 모든 값들을 1에서 빼준다
    for j in range(19):
        board[row][j] = 1 - board[row][j]

    # 바둑판의 모든 row의 col 위치에서 값을 바꿔준다
    for j in range(19):
        board[j][col] = 1 - board[j][col]

# print하기
for i in range(len(board)):
    row = board[i]
    for j in row:
        print(j, end=" ")

    # 각 줄이 끝나면 한줄 엔터!
    print()