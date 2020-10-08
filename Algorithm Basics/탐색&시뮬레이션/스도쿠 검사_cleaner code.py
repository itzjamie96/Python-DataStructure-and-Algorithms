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
# 틀렸을 때 바로 리턴하고 끝내기 위해 함수 쓰기
def solve(sudoku):
    # 1 ~ 9까지 숫자를 확인하기 위해 check 배열 생성
    # sudoku[i][j]가 인덱스 번호가 되어 그 내용물은 모두 1로 넣어주기
    # 만약 check배열의 sum이 9가 아니면 return False
    
    # 가로세로 먼저 검사
    for i in range(9):
        rowCheck = [0]*10
        colCheck = [0]*10
        
        for j in range(9):
            rowCheck[sudoku[i][j]] = 1
            colCheck[sudoku[j][i]] = 1
        
        # 만약 합이 9가 아니라면 중복이 있었기 때문에 어떤 수의 칸은 비어있는 것
        if sum(rowCheck) != 9 or sum(colCheck) != 9:
            return False

    # 네모 검사
    for i in range(3):
        for j in range(3):
            squareCheck = [0]*10

            for k in range(3):
                for l in range(3):
                    # sudoku[i*3 + k][j*3+l] => row, col
                    squareCheck[sudoku[i*3 + k][j*3+l]] = 1

            if sum(squareCheck) != 9:
                return False

    return True


sudoku = [list(map(int, input().split())) for _ in range(9)]

if solve(sudoku):
    print("YES")
else:
    print("NO")
