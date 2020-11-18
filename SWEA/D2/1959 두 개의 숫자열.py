'''
- 더 긴 쪽 구하기
- 비교 가능한 횟수 i: long-short+1
- for i:
    - short만큼 for loop (j)
        - short[j] * long[i+j] 누적하기
    if 현재 누적 > 기존 최대:
        기존 최대 갱신
'''
T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    nList = list(map(int, input().split()))
    mList = list(map(int, input().split()))

    maxi = 0
    if N > M:
        for i in range(N-M+1):
            tmp = 0
            for j in range(M):
                tmp += mList[j] * nList[i+j]
            if tmp > maxi:
                maxi = tmp
    else:
        for i in range(M - N+1):
            tmp = 0
            for j in range(N):
                tmp += nList[j] * mList[i + j]
            if tmp > maxi:
                maxi = tmp

    print('#{} {}'.format(tc,maxi))



