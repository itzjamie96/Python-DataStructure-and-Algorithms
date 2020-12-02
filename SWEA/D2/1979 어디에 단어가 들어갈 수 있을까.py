'''
- N*N 이차원 리스트 받기
- 가로, 세로로 연속해서 1이 K만큼 나오는지 확인
'''
def checkK(current):
    global cnt
    if Ks in current :
        check = ''
        for i in range(N):
            if check == '':
                if current[i] == '1':
                    check += '1'
            else:
                if current[i] == '1':
                    check += '1'
                    if i == N-1 and len(check) == K:
                        cnt += 1
                else:
                    if len(check) == K:
                        cnt += 1
                        check = ''
                    else:
                        check = ''

# T = 1
T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split())
    board = [''.join(input().split()) for _ in range(N)]

    # 확인할 값
    Ks = '1'*K

    cnt = 0
    for i in range(N):
        checkK(board[i])

    # 세로
    for i in range(N):
        col = ''
        for j in range(N):
            col += board[j][i]
        checkK(col)


    print('#{} {}'.format(tc,cnt))