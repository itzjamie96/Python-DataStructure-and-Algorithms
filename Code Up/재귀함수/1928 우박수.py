def collatz(n):
    print(n)
    if n == 1:
        return
    else:
        if n%2:
            collatz(3*n+1)
        else:
            collatz(n//2)

n = int(input())
collatz(n)
