'''
이건 빙고판
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18

이건 사회자
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15

빙고판엔 0이 없으니까 불리는 수는 다 0으로 만들고 0으로 이뤄진 빙고 3개가 있는지 확인하자!
'''
def bingo(n):
    cnt = 0

    flag = True
    for i in range(5):
        for j in range(5):
            if board[i][j] == n:
                board[i][j] = 0
                flag = False
                break
        if flag == False:
            break

    #빙고 확인
    lDiag = 0
    rDiag = 0
    for i in range(5):
        if sum(board[i]) == 0:
            cnt += 1

        # 대각선
        lDiag += board[i][i]
        rDiag += board[i][4-i]

        #세로
        col = 0
        for j in range(5):
            col += board[j][i]
        if col == 0:
            cnt += 1

    if lDiag == 0:
        cnt +=1
    if rDiag == 0:
        cnt += 1

    if cnt >= 3:
        return True
    else:
        return False


board = [list(map(int, input().split())) for _ in range(5)]

# 사회자는 이차원 배열로 받을 필요가 없으니 한줄로 쭉 받았다
num = []
for _ in range(5):
    num.extend(list(map(int, input().split())))

# 만약 순서대로 부르다가 빙고가 나왔다! 그럼 그 순서(=index+1)프린트 후 break
for i in range(len(num)):
    if bingo(num[i]):
        print(i+1)
        break

