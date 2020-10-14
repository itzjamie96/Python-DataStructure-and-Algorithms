'''
[풀이]
start = 0
end = start + K

while start < end:
if end에 정류장이 없음:
    end -= 1
elif end >= N(완전 끝):
    끝
else: (정류장 있음)
    cnt += 1
    start = end
    end = start + K
'''
T = int(input())
for tc in range(1, T+1):

    # K, N, M을 각자 매핑해서 받는다
    K, N, M = map(int, input().split())

    # 우선 정류장 위치를 임시 tmp 리스트에 받아두고
    tmp = list(map(int, input().split()))

    # 0 ~ N+1까지 있는 빈 리스트를 만들고
    # 정류장 위치를 1로 표시해준다
    # ex) [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  <= 정류장 1, 3, 5, 7, 9
    stations = [0]*(N+1)
    for i in tmp:
        stations[i] = 1
    # print(stations)

    # 시작위치와 끝 위치를 정해준다
    start = 0
    end = start + K     #끝 위치는 시작+K번째 인덱스가 될 거임
    cnt = 0             # 충전횟수를 셀 변수

    '''
    먼저 끝 위치를 확인한다
    
    정류장의 끝 위치(stations[end])에 정류장이..
        - 있다! => 충전 + 1, 시작위치 = 현재 끝위치, 끝 위치 다시 시작 +K 로 갱신해줌
        - 없다! => 끝 위치 - 1
    '''
    while start < end and end <N:

        if stations[end] == 1:
            cnt += 1
            start = end
            end = start+K
        else:
            end -= 1

    '''
    while문이 끝났는데 end랑 start랑 같다면?
    이러면 start ~ end 구간 내에 정류장이 없어서 충전을 못한거다
      => 정류장을 못찾아서 end-1 하면서 찾아도 못 찾은 것
    결론: 구간내 가능한 정류소 없음: cnt = 0
    '''
    if end == start:
        cnt = 0

    print('#{} {}'.format(tc, cnt))