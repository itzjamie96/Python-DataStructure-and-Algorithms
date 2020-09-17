'''
마구간 정하기

N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며,
마구간간에 좌표가 중복되는 일은 없습니다.
현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다.
각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을 마구간에 배치하고 싶습니다.
C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가
최대가 되는 그 최대 값을 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다.
둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩 주어집니다.

▣ 출력설명
첫 줄에 가장 가까운 두 말의 최대 거리를 출력하세요.

▣ 입력예제 1
5 3
1
2
8
4
9

▣ 출력예제 1
3
'''
# 길이에 맞게 말들 배치시키는 함수
def locate(distance):
    cnt = 1
    horse = 0
    for i in range(1, N):
        if stables[i] - stables[horse] >= distance:
            cnt += 1
            horse = i

    return cnt
# N은 마구간, C는 말 갯수
N, C = map(int, input().split())

# 마구간 입력받기
stables = []
for _ in range(N):
    stables.append(int(input()))

# 마구간 정렬
stables.sort()

# 이분탐색을 위한 시작과 끝
start = 1   # 최소 거리
end = stables[N-1]  #마지막 마구간 위치 = 최대 거리

ans = 0

while start < end:
    mid = (start+end)//2

    # 주어진 마리수보다 더 많이 배치 할 수 있어도 답이 가능
    if locate(mid) >= C:
        ans = mid   # 거리 킵
        start = mid + 1     # 더 큰 거리 찾기 = start 이동

    else:
        end = mid - 1   # 범위 좁히기 = end 이동

print(ans)