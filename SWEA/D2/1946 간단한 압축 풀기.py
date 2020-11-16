'''
- result는 []
- alpha, n으로 매핑 받기
- n이 10의 배수면 n//10 만큼 alpha*10를 result에 추가해주기
- 아니라면 n//10만큼 ''에 넣어두고 공백이 얼만큼 남았는지 확인 (=left)
- left가 0보다 크면 alpha*left를 result[-1]에 추가 후 n -= left
-
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = []

    print('#{}'.format(tc))

    left = 0
    for _ in range(N):
        alpha, n = map(str, input().split())
        n = int(n)

        if left > 0:
            result[-1] += alpha*left
            n -= left
            left = 0

        if n%10 == 0:
            for i in range(n//10):
                result.append(alpha*10)

        else:
            for i in range(n//10):
                result.append(alpha*10)
            result.append(alpha*(n%10))
            left = 10 - (n%10)

    print(*result, sep='\n')

