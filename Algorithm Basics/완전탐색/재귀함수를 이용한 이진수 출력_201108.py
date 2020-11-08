def toBinary(N):
    global result
    if N//2==0:
        result = str(N%2) + result
        return
    else:
        result = str(N%2) + result
        toBinary(N//2)

N = int(input())
result = ''
toBinary(N)
print(result)