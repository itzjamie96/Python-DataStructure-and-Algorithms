'''
격자판 회문수

1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는 세로방향으로
길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.

▣ 입력설명
1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.

▣ 출력설명
5자리 회문수의 개수를 출력합니다.

▣  입력예제 1
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5

▣  출력예제 1
3
'''
# 7*7 격자판임
board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(3):
    for j in range(7):
        row = board[i][j:j + 5]

        if row == row[::-1]:
            cnt += 1

        #세로
        for k in range(2):
            # 세로로 앞에 2개랑 뒤에서 2개
            if board[i+k][j] != board[i+5-k-1][j]:
                break

        else:
            cnt += 1


print(cnt)


