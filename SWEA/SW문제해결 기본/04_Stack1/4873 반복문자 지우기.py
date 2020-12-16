'''

'''
T = int(input())
for tc in range(1, T+1):

    text = input()

    i = 0
    while True:
        if i == len(text)-1:
            break
        else:
            if text[i] == text[i + 1]:
                text = text[:i] + text[i + 2:]
                i = 0
            else:
                i += 1
    print('#{} {}'.format(tc, len(text)))
