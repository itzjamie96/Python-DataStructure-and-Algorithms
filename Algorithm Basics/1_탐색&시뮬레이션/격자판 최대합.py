'''
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의  합 중  가 장 큰 합을 출력합니다.

▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.

▣ 출력설명
최대합을 출력합니다.

▣  입력예제 1
5
10 13 10 12 15
12 39 30 23	11
11 25 50 53	15
19 27 29 37	27
19 13 30 13	19

▣  출력예제 1
155
'''
N = int(input())

# 격자판 입력받기
board = [list(map(int, input().split())) for _ in range(N)]

maxi = -2147000000

###########가로세로 먼저###############
# col은 세로로
for col in range(N):

    rowSum = colSum = 0

    # row은 가로로 움직인다ㅏㅏㅏ
    for row in range(N):

        # col 고정 row가 변동
        rowSum += board[col][row]

        # row 고정 col이 변동
        # row는 계속 증가 => row 증가 끝나면 col이 바뀜!
        colSum += board[row][col]

        # row가 다 돌면 가로세로 sum은 한줄씩 구해진거
        if rowSum > maxi:
            maxi = rowSum
        if colSum > maxi:
            maxi = colSum

##################대각선#####################
leftDown = rightUp = 0
for i in range(N):
    # 왼쪽 아래로 가는 대각선은 i=j
    leftDown += board[i][i]

    # 오른쪽 위로 가는 대각선은 사실 오른쪽 맨 끝에서 왼쪽 아래로 쭈루룩 떨어지는거
    # 세로로 있는 리스트의 마지막 요소부터 하나씩
    # 참고로 마지막 인덱스는 N-1
    rightUp += board[i][N-1-i]

if leftDown > maxi:
    maxi = leftDown
if rightUp > maxi:
    maxi = rightUp

print(maxi)