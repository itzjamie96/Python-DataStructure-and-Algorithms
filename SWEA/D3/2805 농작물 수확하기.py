T = int(input())

for tc in range(1, T+1):

    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    # print(*farm, sep='\n')

    mid = N//2              #중간값
    start, end = mid, mid   #시작위치 = 네모 정가운데
    total = 0               #합 누적할거

    for i in range(N):
        for j in range(start, end+1):
            total += farm[i][j]

        if i<mid:
            start -= 1
            end += 1

        else:
            start += 1
            end -= 1

    print(total)