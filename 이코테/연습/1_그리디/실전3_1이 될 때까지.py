'''
N이 1이 될 때까지
--> N - 1
--> (N % K == 0) N//K
최소횟수 구하기

N%K번 -1
이후 N//K
'''
N, K = map(int, input().split())

cnt = N%K
N -= cnt
while N != 1:
    N //= K
    cnt += 1

print(cnt)


'''
25 5
=== 2
'''