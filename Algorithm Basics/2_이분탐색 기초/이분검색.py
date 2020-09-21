'''
이분검색

임의의 N개의 숫자가 입력으로 주어집니다.
N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개의 수인 M이 주어지면
이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는 프로그램을 작성하세요.
단 중복값은 존재하지 않습니다.

▣ 입력설명
첫 줄에 한 줄에 자연수 N(3<=N<=1,000,000)과 M이 주어집니다.
두 번째 줄에 N개의 수가 공백을 사이에 두고 주어집니다.

▣ 출력설명
첫 줄에 정렬 후 M의 값의 위치 번호를 출력한다.

▣ 입력예제 1
c

▣ 출력예제 1
3

[풀이]
- N과 M을 입력받음
- 숫자 리스트 입력받음 => 정렬
- mid == 숫자리스트 길이//2
- M과 mid 비교 => M이 더 작으면 숫자리스트는 0~mid까지. M이 더 크면 숫자리스트는 mid~끝까지
- 반복
'''
N, M = map(int, input().split())

nList = list(map(int, input().split()))
nList.sort()
# print(nList)

start = 0
end = len(nList)-1

flag = True
while flag:

    mid = (start+end)//2

    # M이 더 작을 때는 왼쪽만 탐색
    if M < nList[mid]:
        end = mid-1

    elif M > nList[mid]:
        start = mid+1

    else:
        print(mid+1)
        flag = False



