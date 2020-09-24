
N = int(input())

nlist = list(map(int, input().split()))

maxi = 0

# 커지는 수열 길이 계산
bigger = 1
for i in range(N - 1):
    if nlist[i] <= nlist[i+1]:
        bigger += 1

    else:                   # 잘 가다가 끊기면 현재 최대랑 현재 길이 비교
        if bigger > maxi:
            maxi = bigger
        bigger = 1          # 그 뒤에 수열이 더 있을 수 있으니 bigger 초기화

# 증가 수열 다 끝날 때까지 쭉 증가했다면 최대랑 한번 더 비교
if bigger > maxi:
    maxi = bigger
    
# 작아지는 수열 길이 계산
smaller = 1
for i in range(N-1):
    if nlist[i] >= nlist[i+1]:
        smaller += 1
    else:
        if smaller > maxi:
            maxi = smaller
        smaller = 1

if smaller > maxi:
    maxi = smaller

print(maxi)