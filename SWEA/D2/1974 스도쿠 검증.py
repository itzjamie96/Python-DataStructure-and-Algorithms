def check():
    global flag  # 전역에 있는걸 바꾸려면 global로 불러야함

    # row check
    for i in range(9):

        visit = [0] * (9 + 1)

        for j in range(9):
            # sudoku[i][j]값이 인덱스가 되는 것
            visit[sudoku[i][j]] += 1

            # 1 이상 = 2번 나옴 = 스도쿠 아님!
            if visit[sudoku[i][j]] > 1:
                flag = 0  # 아니라고 표시 후 바로 리턴 = 함수 종료
                return

    # col check
    for i in range(9):
        visit = [0] * (9 + 1)
        for j in range(9):
            visit[sudoku[j][i]] += 1
            if visit[sudoku[j][i]] > 1:
                flag = 0
                return

    # 3 x 3
    for i in range(0, 9, 3):  # 가로로 3씩 점프
        for j in range(0, 9, 3):  # 세로로 3씩 점프
            visit = [0] * (9 + 1)

            for k in range(3):
                for l in range(3):
                    visit[sudoku[k + i][l + j]] += 1

                    if visit[sudoku[k + i][l + j]] > 1:
                        flag = 0
                        return


T = int(input())

for tc in range(1, T + 1):
    flag = 1

    sudoku = [list(map(int, input().split())) for _ in range(9)]

    check()
    print('#{} {}'.format(tc, flag))