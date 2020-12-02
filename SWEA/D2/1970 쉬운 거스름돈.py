'''
******제약사항에 위배되는 input이 많음!********
2. N의 마지막 자릿수는 항상 0이다. (ex : 32850) << 이거에 해당되지 않는 input이 아주 많음
- 이걸 해결하기 위해서 모든 1의 자리 수를 0으로 바꿨다

- money: 돈 종류를 모두 담은 리스트 (큰 돈 ~ 작은 돈 순서로 정렬)
- result: money과 같은 길이의 리스트 (내용물 모두 0)
- money의 0번째부터 주어진 돈을 나눠봄
    - 나눴을 때 0이라면 안 나눠지는 것 => i+1
    - 나눠지면 그 나머지가 N이 됨
    - result[i]에는 몫이 들어감
'''
T = int(input())
for tc in range(1, T+1):

    # 거스름돈
    N = input()
    N = int(N[:len(N)-1]+'0')
    # print(N)

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0]*len(money)

    i = 0
    while i < len(money) or N > 0:

        if N // money[i] != 0:
            result[i] += N//money[i]
            N = N%money[i]

        else:
            i += 1

    print('#{} '.format(tc))
    print(*result)

