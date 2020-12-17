def maxWeight(idx, currWeight, soFar):
    global maxi
    if currWeight > C:
        return
    elif idx >= N:
        if maxi < currWeight:
            maxi = currWeight
        return
    elif currWeight + total - soFar < maxi:
        return
    else:
        maxWeight(idx+1, currWeight+dogs[idx], soFar+dogs[idx])
        maxWeight(idx+1, currWeight, soFar+dogs[idx])

C, N = map(int, input().split())
dogs = [int(input()) for _ in range(N)]

total = sum(dogs)
maxi = 0
maxWeight(0,0,0)
print(maxi)