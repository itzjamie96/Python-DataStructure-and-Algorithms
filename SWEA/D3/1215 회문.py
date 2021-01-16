def findPalindrome(doubleArr, length):
    cnt = 0
    for i in range(8):
        for j in range(8-length+1):
            row = col = ""
            for k in range(length):
                row += doubleArr[i][j+k]
                col += doubleArr[j+k][i]
            if row == row[::-1]:
                cnt += 1
            if col == col[::-1]:
                cnt += 1
    return cnt

for tc in range(1, 11):
    length = int(input())
    board = [input() for _ in range(8)]
    print(f'#{tc} {findPalindrome(board, length)}')
