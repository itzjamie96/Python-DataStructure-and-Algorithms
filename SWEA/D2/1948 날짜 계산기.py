'''
28, 30, 31 에 해당하는 달만 따로 정리해둔다 (딕셔너리)
- 같은 달 일 때
    - day-day 리턴
- 다른 달 일 때 (무조건 두번째 달이 더 큼)
    - 첫 번째 전체day - 현재 day
    - 1 증가한 달의 day ... 두번째 달 -1까지 day만 합치기
    - 두번째 day
    - 위에 세개 합치기
'''
days = {
    1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
    7:31, 8:31, 9:30, 10:31, 11:30, 12:31
}
T = int(input())
for tc in range(1, T+1):

    fm, fd, sm, sd = map(int, input().split())

    print('#{}'.format(tc), end=' ')
    if fm == sm:
        print(sd-fd+1)
    else:
        total = days[fm]-fd
        for month in range(fm+1, sm):
            total += days[month]
        total += sd
        print(total+1)