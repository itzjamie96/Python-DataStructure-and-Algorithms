'''
스토쿠 검사

스도쿠는 매우 간단한 숫자 퍼즐이다. 9×9 크기의 보드가 있을 때,
각 행과 각 열, 그리고 9개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복없이 나타나도록
보드를 채우면 된다.

완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 "YES",
잘못 풀었으면 "NO"를 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.

▣ 출력설명
첫째 줄에 “YES" 또는 ”NO"를 출력하세요.

▣ 입력예제 1
1 4	3 6	2 8	5 7	9
5 7	2 1	3 9	4 6	8
9 8	6 7	5 4	2 3	1
3 9	1 5	4 2	7 8	6
4 6	8 9	1 7	3 5	2
7 2	5 8	6 3	9 1	4
2 3	7 4	8 1	6 9	5
6 1	9 2	7 5	8 4	3
8 5	4 3	9 6	1 2	7

▣ 출력예제 1
YES
'''
def check(sudoku):

    ##########가로세로
    for r in range(9):
        row, col = [], []
        for c in range(9):
            # 가로
            if sudoku[r][c] not in row and 0<sudoku[r][c]<10:
                row.append(sudoku[r][c])
            else:
                return "NO"
                # return 0
            # 세로
            if sudoku[c][r] not in col and 0<sudoku[c][r]<10:
                col.append(sudoku[c][r])
            else:
                return "NO"
                # return 0

    #############네모 검사
    for i in range(0, 10, 3):   #세로
        square = []
        for m in range(0, 10, 3):   #가로

            for j in range(3):
                for k in range(3):
                    if sudoku[j][k] not in square and 0<sudoku[j][k]<10:
                        square.append(sudoku[j][k])
                    else:
                        return "NO"
                        # return 0
            square.clear()
    # return 1
    return "YES"

# T = int(input())
# for tc in range(1, T+1):

sudoku = [list(map(int, input().split())) for _ in range(9)]
    # print('#{} {} '.format(tc, check(sudoku)))
print(check(sudoku))