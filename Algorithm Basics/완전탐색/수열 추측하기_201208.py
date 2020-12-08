def getPerm(level, sum):
    if level == N and sum == F:
        print(*perm)
        exit()

    else:
        for i in range(1, N+1):
            if check[i] == 0:
                check[i] = 1
                perm[level] = i
                getPerm(level+1, sum+perm[level]*pattern[level])
                check[i] = 0


# 1~N, F=파스칼을 활용한 합
N, F = map(int, input().split())

perm = [0]*N       # 순열
pattern = [1] * N  # 파스칼에 따른 패턴
check = [0]*(N+1)

for i in range(1, N):
    pattern[i] = pattern[i - 1] * (N - i) // i

getPerm(0,0)