'''
500원, 100원, 50원, 10원으로 N원을 거슬러주기
N은 항상 10의 배수
'''

coins = [500, 100, 50, 10]

N = 1260
cnt = 0

for coin in coins:
    cnt += N//coin
    N %= coin

print(cnt)
