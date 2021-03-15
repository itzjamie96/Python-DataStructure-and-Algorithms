N = int(input())
heights = list(map(int, input().split()))
M = int(input())

heights = [[h, idx] for idx, h in enumerate(heights)]

for i in range(M):
    max_idx = max(heights)[1]
    min_idx = min(heights)[1]

    heights[max_idx][0] -= 1
    heights[min_idx][0] += 1

print(max(heights)[0] - min(heights)[0])