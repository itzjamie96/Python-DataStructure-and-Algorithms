for tc in range(10):
    t = int(input())
    N, M = map(int, input().split())
    result = 1
    for i in range(M):
        result *= N
    print(f'#{t} {result}')