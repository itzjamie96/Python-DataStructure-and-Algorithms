'''
이진탐색
1. 시작, 끝, 목표가 주어진다
2. 시작+끝//2가 목표보다 크면 시작위치를 (시작+끝//2)+1로 조정한다 (끝은 그대로 둠)
3. 시작+끝//2가 목표보다 작으면 끝 위치를 (시작+끝//2)-1로 조정한다
4. 목표를 찾기까지 시작/끝 위치를 조정한 횟수를 리턴한다
'''
def binarySearch(start, end, goal):
    cnt = 0
    while start < end:
        mid = (start+end)//2
        if goal > mid:
            start = mid
            cnt += 1
        elif goal < mid:
            end = mid
            cnt += 1
        else:
            return cnt

T = int(input())
for tc in range(1, T+1):

    # 전체페이지, A의 목표, B의 목표가 주어진다
    P, A, B = map(int, input().split())

    a, b = binarySearch(1, P, A), binarySearch(1, P, B)
    # print(a, b)

    if a < b:
        print('#{} A'.format(tc))
    elif a > b:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))


