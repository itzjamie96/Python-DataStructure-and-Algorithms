'''
N*N에서 M*M의 합 중 가장 큰 합 구하기
N-M+1씩 이동 가능

'''
# T = 1
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    square = [list(map(int, input().split())) for _ in range(N)]
    # print(*square, sep='\n')

    maxi = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            current = 0
            for k in range(M):
                for l in range(M):
                    current += square[j+l][i+k]
            if current > maxi:
                maxi = current
    print('#{} {}'.format(tc, maxi))

