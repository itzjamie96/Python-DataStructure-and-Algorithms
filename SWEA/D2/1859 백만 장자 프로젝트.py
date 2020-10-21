'''
- 맨 마지막 날은 어쨌든 팔아야하니까 keep한다 (sellingPrice)
- N-2번째부터 뒤로 for문을 돌린다 (방금 N-1은 keep 했으니까)
- 하나씩 이동하면서 만약 현재 값이 sellingPrice보다 작으면 (-현재값)+sellingPrice를 result에 더해준다
- 만약 현재 값이 sellingPrice보다 크면 그 값으로 sellingPrice를 갱신해준다
'''
T = int(input())
for tc in range(1, T+1):

    N = int(input())
    prices = list(map(int, input().split()))

    sellingPrice = prices[N-1]
    result = 0

    for i in range(N-2, -1, -1):
        if prices[i] > sellingPrice:
            sellingPrice = prices[i]
        else:
            result += -prices[i] + sellingPrice

    print('#{} {}'.format(tc, result))