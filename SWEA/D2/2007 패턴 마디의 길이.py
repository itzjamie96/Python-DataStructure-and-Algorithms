'''
문자에서 반복되는 부분을 찾아서 길이 출력하기
'''
# T = 1
T = int(input())
for tc in range(1, T+1):

    string = input()

    pList = []
    for i in range(1, 11):
        pList.append(string[:i])

    ans = 10
    for i in range(10):
        tmp = len(pList[i])

        if string[:tmp] == string[tmp:2 * tmp]:
            if tmp < ans:
                ans = tmp
                break
    print('#{} {}'.format(tc, ans))