# 회문 찾기 함수
def findPalindrome(doubleArr, length):
    cnt = 0
    for i in range(8):
        # 8-길이+1 = 가로/세로로 범위를 벗어나지 않고 주어진 길이를 확인할 수 있는 최대
        for j in range(8-length+1):
            row = col = ""
            # 주어진 길이만큼 for문을 돈다
            for k in range(length):
                row += doubleArr[i][j+k]
                col += doubleArr[j+k][i]
            # 회문이 맞다면 cnt+1
            if row == row[::-1]:
                cnt += 1
            if col == col[::-1]:
                cnt += 1
    return cnt

for tc in range(1, 11):
    length = int(input())
    board = [input() for _ in range(8)]
    print(f'#{tc} {findPalindrome(board, length)}')
