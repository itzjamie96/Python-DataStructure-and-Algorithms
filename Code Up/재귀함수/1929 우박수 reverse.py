def reversedCollatz(n):
    if n == 1:
        print(n)
        return
    else:
        if n%2:
            reversedCollatz(3*n+1)
        else:
            reversedCollatz(n//2)
    print(n)

n = int(input())
reversedCollatz(n)