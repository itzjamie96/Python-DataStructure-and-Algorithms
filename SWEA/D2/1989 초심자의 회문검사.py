'''
- 단어를 str으로 받아서 뒤집은거랑 똑같은지 확인한다
- 같으면 1, 아니면 0 출력
'''
T = int(input())
for tc in range(1, T+1):

    word = input()
    if word == word[::-1]:

        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))