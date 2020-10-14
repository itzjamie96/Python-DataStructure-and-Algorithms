T = int(input())
for tc in range(1, T+1):

    N = int(input())

    # 카드 리스트를 입력받는다
    cards = list(map(int, input()))

    # 딕셔너리를 만든다
    cDict = dict()

    for card in cards:

        # 만약 딕셔너리에 카드번호가 있으면 get해서 +1해서 value에 넣어주고
        if card in cDict.keys():
            val = cDict.get(card)
            cDict[card] = val + 1
        # 딕셔너리 키에 없는 카드번호면 그냥 value에 1을 넣어준다
        else:
            cDict[card] = 1

    # 딕셔너리의 value 중 가장 큰 걸 찾아서 key랑 value를 출력한다!
    #     - 만약 큰 값이 다 똑같으면 더 큰 key를 출력한다!
    maxi = 0
    key = 0
    for k, v in cDict.items():
        if v > maxi:
           key = k
           maxi = v
        elif v == maxi:
            if k > key:
                key = k

    print('#{} {} {}'.format(tc, key, maxi))