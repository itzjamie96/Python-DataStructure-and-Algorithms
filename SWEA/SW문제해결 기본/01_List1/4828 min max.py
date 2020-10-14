'''
직접 min, max 함수 구현하기

[min]
mini = 2147000000
maxi = -2147000000
배열의 하나씩 돌면서 만약 현재 값이 mini보다 작다면 mini 갱신 + maxi보다 크다면 maxi 갱신
'''

# min과 max를 찾아서 그 두개의 차를 돌려주는 함수
def findMinMax(arr):
    
    # 아주! 큰 수와 아주! 작은 수를 최대, 최소값을 담을 변수에 넣는다
    mini = 2147000000   
    maxi = -2147000000

    # 입력받은 리스트의 모든 요소를 첫번째부터 마지막까지 하나씩 확인할거다
    for num in arr:
        
        # 만약 현재 요소가 위에서 설정한 mini보다 작다면 mini의 값을 현재 요소로 바꿔준다
        if num < mini:
            mini = num

        # 만약 현재 요소가 위에서 설정한 maxi보다 크다면 maxi의 값을 현재 요소로 바꿔준다
        elif num > maxi:
            maxi = num

    # for문이 다 끝나면 maxi와 mini 값이 나온다
    # 두 개의 차를 리턴한다
    return maxi-mini

T = int(input())
for tc in range(1, T+1):

    # 리스트의 크기
    N = int(input())

    # 각 숫자를 입력받아서 리스트에 넣어준다
    numList = list(map(int, input().split()))

    # 함수로 최대-최소를 구해서 그걸 result에 넣는다
    result = findMinMax(numList)

    # BAAM 답이 나온다
    print('#{} {}'.format(tc, result))