import sys

N = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))

# 수열 미리 자리만들어두기
seq = [0]*N

for i in range(N):
    for j in range(N):

        if nlist[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break

        elif seq[j] == 0:
            nlist[i] -= 1

print(*seq)