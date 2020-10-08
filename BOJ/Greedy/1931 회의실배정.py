'''
회의 많이 = 회의끝나는 시간이 빠른(?) 애 위주로

이거 또 풀어봐야함
'''
import sys

N = int(sys.stdin.readline())
meetings = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())

    # 끝나는 시간 기준으로 정렬해야하니까 끝나는 애를 앞에 놔주기~
    meetings.append((end, start))

# 데이터 순서가 어찌될지 모르니 정렬해주기~
meetings.sort()

endTime = 0 #keep할 끝나는 시간
cnt = 0     #회의 총 몇개인지

for end, start in meetings:
    if start >= endTime:    #시작시간이 끝나는 시간보다 같거나 크면 회의 가능
        endTime = end       #끝나는시간 갱신해주고
        cnt += 1            #회의 갯수 하나 추가해주기

print(cnt)
