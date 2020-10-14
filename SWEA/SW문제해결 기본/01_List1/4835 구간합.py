
T = int(input())
for tc in range(1, T+1):

    N, M = map(int, input().split())
    numList = list(map(int, input().split()))
    
    # 합들을 담을 리스트
    sums = []

    '''
    N-M+1 만큼 for문을 돌린다는 것:
        [1, 2, 3, 4]에서 2개씩 합을 구한다고 하면
        1+2, 2+3, 3+4 이렇게 3개가 나올 수 있다.
        그럼 1,2,3,4 중에서 1, 2, 3까지만 for문이 돌게 된다.
        즉, 4-2+1 번 for문이 도는 것! == N-M+1
    '''
    for i in range(N-M+1):
        tmp = 0
        # i번째부터 M개를 다 tmp에 더해준다
        for j in range(M):
             tmp += numList[i+j]

        # 합 리스트에 tmp 값을 넣어준다!
        sums.append(tmp)

    # 각각 min max구하기보다 그냥 정렬해서 맨 뒤에꺼에서 맨 앞에꺼를 빼주면 된다
    sums = sorted(sums)
    print('#{} {}'.format(tc, sums[len(sums)-1] - sums[0]))