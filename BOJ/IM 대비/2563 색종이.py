'''
100 * 100 종이에다가
색종이 영역은 1로 표기 (10*10)
1 다 더하기
'''
def color(x, y):
    for i in range(10):
        for j in range(10):
            board[x+i][y+j] = 1

board = [[0 for _ in range(100)] for _ in range(100)]
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    color(x,y)

total = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            total += 1

print(total)
