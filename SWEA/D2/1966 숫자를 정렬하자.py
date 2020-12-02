T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    print('#{}'.format(tc), end=' ')
    print(*arr)