'''
1. str1을 set으로 받는다 (중복제거)
2. str1애들로 딕셔너리를 만든다
3. str1의 각 요소에 대해서 str2에 몇개씩 있는지 카운트 후 딕셔너리에 추가한다
4. 딕셔너리의 value중 가장 큰 값을 출력한다
'''
T = int(input())
for tc in range(1, T+1):

    str1 = set(input())
    str2 = input()

    countAlpha = {}
    for alphabet in str2:
        if alphabet in str1:
            if alphabet in countAlpha.keys():
                value = countAlpha.get(alphabet)
                countAlpha[alphabet] = value+1
            else:
                countAlpha[alphabet] = 1

    print('#{} {}'.format(tc, max(countAlpha.values())))