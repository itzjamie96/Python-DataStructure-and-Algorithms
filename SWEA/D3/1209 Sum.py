def findMaxSum(arr):
    rowMax, colMax, rightDown, leftDown = 0, 0, 0, 0
    for i in range(100):
        # find rowMax
        if sum(arr[i]) > rowMax:
            rowMax = sum(arr[i])
        #colMax
        tmpCol = 0
        for j in range(100):
            tmpCol += arr[j][i]
        if tmpCol > colMax:
            colMax = tmpCol
        # diagonals
        rightDown += arr[i][i]
        leftDown += arr[i][99-i]

    return max(rowMax, colMax, rightDown, leftDown)

for tc in range(10):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{N} {findMaxSum(board)}')