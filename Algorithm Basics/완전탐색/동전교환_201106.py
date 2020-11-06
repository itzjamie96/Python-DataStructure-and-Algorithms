'''
동전 종류 갯수: 3
동전 종류: 1 2 5
거슬러 줘야 하는 금액: 15

동전: [5,2,1]  << 역순으로 해야 동전 갯수 적어짐

종료:
- 금액보다 클 때
- 지금 있는 거스름돈 갯수보다 클 때

currentSum = currentSum + 현재 동전

'''
def countChange(coinNum, currentSum):
    global result

    if currentSum > M:
        return

    elif currentSum == M:
        if coinNum < result:
            result = coinNum
        return

    elif coinNum > result:
        return

    else:
        for i in range(N):
            countChange(coinNum+1, currentSum+coins[i])

N = int(input())
coins = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
result = 2147000000
countChange(0, 0)

print(result)
