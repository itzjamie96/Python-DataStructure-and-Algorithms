'''
가장 기본적인 이분탐색
1. 주어진 숫자 리스트(=영역)을 정렬
2. 시작과 끝점 정해주기
3. mid(중간값)을 계산해서 찾는 수(=x)랑 비교
    - 만약 x가 mid보다 크면 x는 mid 기준 오른편에 존재
    - 만약 x가 mid보다 작으면 x는 mid 기준 왼편에 존재
4. 각 상황에 맞게 start나 end 조정 후 반복

*** 배열 인덱스랑! 값이랑! 헷갈리지! 않기!!!!!! 인덱스의 값을 찾아야지 인덱스 찾으면 안됨!!!!
'''

# 이분탐색 함수
def binarySearch(x):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end)//2

        if x > nList[mid]:
            start = mid + 1
        elif x < nList[mid]:
            end = mid - 1
        else:
            return 1
    return 0

N = int(input())
nList = list(map(int, input().split()))
nList.sort()

M = int(input())
mList = list(map(int, input().split()))

for i in mList:
    print(binarySearch(i))

