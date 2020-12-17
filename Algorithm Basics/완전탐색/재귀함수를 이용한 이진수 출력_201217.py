def toBinary(n):
    global result
    if n == 1:
        result = str(n) + result
        print(result)
        return
    else:
        result = str(n%2) + result
        n //= 2
        toBinary(n)

N = int(input())
result = ''
toBinary(N)