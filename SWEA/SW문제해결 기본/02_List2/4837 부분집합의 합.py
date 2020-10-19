'''
부분집합을 빠르게 구한다 (비트연산자 활용)
만약 현재 부분집합의 갯수가 N, 합이 K면 cnt+1
'''
T = int(input())
for tc in range(1, T+1):

    A = list(range(1, 13))
    N, K = map(int, input().split())

    cnt = 0
    for i in range(1 << len(A)):
        currentSet = []
        for j in range(len(A)):
            if i & (1 << j):
                currentSet.append(A[j])
        if len(currentSet) == N and sum(currentSet) == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
