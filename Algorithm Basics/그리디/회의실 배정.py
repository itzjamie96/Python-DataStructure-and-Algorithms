'''
- 회의가 끝나는 시간을 기준으로 정렬해야함
- 시작 시간 빨라봤자 상관없음 (목표는 최대한 많은 회의)
- 끝나는 시간보다 시작시간이 크거나 같으면 진행 가능 ==> 카운트
'''
import sys

N = int(sys.stdin.readline())
meetings = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end))

# x의 1번이 우선순위, 그 다음이 x의 0번
meetings.sort(key=lambda x:(x[1], x[0]))

endT = 0
cnt = 0

for start, end in meetings:
    if start >= endT:
        endT = end
        cnt += 1

print(cnt)


