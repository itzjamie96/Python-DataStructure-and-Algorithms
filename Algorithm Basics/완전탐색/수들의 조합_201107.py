'''
어떤 숫자들의 K개 조합의 합이 M의 배수인 경우 세기
5 3
2 4 5 8 12
6

'''
def combination(current):
    global cnt
    if current == K:
        # print(combi)
        tmp = sum(combi)
        if tmp not in tmpSum and tmp%M == 0:
            tmpSum.append(tmp)
            # print(tmp)
            cnt+=1
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = numList[i]
                combi[current] = numList[i]
                combination(current+1)
                visited[i] = 0

N, K = map(int, input().split())
numList = list(map(int, input().split()))
visited = [0]*(N+1)
combi = [0]*K
M = int(input())
cnt = 0
tmpSum = []
combination(0)
print(cnt)