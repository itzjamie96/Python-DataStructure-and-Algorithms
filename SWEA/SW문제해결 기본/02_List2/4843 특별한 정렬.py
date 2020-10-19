'''
1. 주어진 리스트를 정렬한다 (큰거 - 작은거)
2. 결과 리스트에 맨앞, 맨뒤 순서로 넣는다
    - i번째, N-1-i번째
    - for문은 5까지만 해도 됨(어짜피 10개만 출력함)
3. 결과리스트 출력하기
'''
T = int(input())
for tc in range(1, T+1):

    N = int(input())
    numList = list(map(int, input().split()))
    
    # 큰거 ~ 작은거 순으로 정렬하기
    numList = sorted(numList, reverse=True)
    
    # 결과 담을 리스트
    result = []
    
    # 어짜피 10개만 출력하니까 5번째 인덱스까지만 돌린다
    for i in range(5):
        result.append(numList[i])
        result.append(numList[N-1-i])

    print('#{}'.format(tc), end=' ')
    print(*result)
