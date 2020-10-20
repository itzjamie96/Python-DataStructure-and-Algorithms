def findVertical():

    for i in range(N-M+1):
        tmp = []
        for j in range(N):
            for k in range(M):
                tmp.append(board[k+i][j])
            # print(tmp)
            if len(tmp) == M and tmp == tmp[::-1]:
                return tmp

            tmp.clear()


T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())

    board = []
    isDone = False
    for _ in range(N):
        tmp = list(map(str, input()))

        for i in range(N-M+1):
            if tmp[i:] == tmp[i:][::-1]:
                print('#{}'.format(tc), end=' ')
                print(*tmp[i:], sep='')
                isDone = True
        else:
            board.append(tmp)
    # print(*board, sep='\n')
    # print()

    # 가로 통과 못했을 때만 세로 확인
    if isDone == False:
        vertical = findVertical()
        print('#{}'.format(tc), end=' ')
        print(*vertical, sep='')

