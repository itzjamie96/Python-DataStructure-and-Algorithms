N = int(input())
meetings = []
for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((end, start))

meetings = sorted(meetings)

result = 1
current_end, current_start = meetings[0]
for i in range(1, N):
    end, start = meetings[i]
    if start >= current_end:
        result += 1
        current_end, current_start = end, start

print(result)