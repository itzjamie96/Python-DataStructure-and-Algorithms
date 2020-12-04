'''
- 1부터 N까지 홀수는 더하고 짝수는 뺀다
'''
T = int(input())
for tc in range(1, T+1):

    N = int(input())
    result = 0
    for i in range(1, N+1):
        if i%2:
            result += i
        else:
            result -= i
    print('#{} {}'.format(tc, result))