'''
- N을 받는다
- 2, 3, 5, 7, 11 로 N을 나눠본다
    - 나머지가 0이면 N = N//나눈 수
    - a, b, c, d, e 중 해당하는 수에 +1 (리스트로 구하기)
'''

T = int(input())
for tc in range(1, T+1):

    result = [0]*5

    N = int(input())

    while N > 1:

        if N % 2 == 0:
            N = N//2
            result[0] += 1

        if N % 3 == 0:
            N = N//3
            result[1] += 1

        if N % 5 == 0:
            N = N//5
            result [2] += 1

        if N % 7 == 0:
            N = N//7
            result[3] += 1

        if N % 11 == 0:
            N = N//11
            result[4] += 1
    print('#{} '.format(tc), end='')
    print(*result)