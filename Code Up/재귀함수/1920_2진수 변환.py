import sys

def toBinary(N):
    global binary
    if N == 0:
        binary.append(0)
        return

    if N == 1:
        binary.append(N%2)
        return
    else:
        binary.append(N%2)
        toBinary(N//2)

N = int(sys.stdin.readline())
binary = []
toBinary(N)

print(*binary[::-1], sep='')

