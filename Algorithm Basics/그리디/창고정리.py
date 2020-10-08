'''
- max, min 구하기
- max-1, min+1
- 반복 N회
- max, min 구해서 차이 구하기

- sort m번 하는 것보다 뭐가 더 빠를지 확인해보기
'''
def findMinMax(arr):
    mini = 21479600
    minidx = maxidx = 0
    maxi = 0
    for i in range(N):
        if arr[i] < mini:
            mini = arr[i]
            minidx = i

        if arr[i] > maxi:
            maxi = arr[i]
            maxidx = i

    return maxidx, minidx

import sys

N = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

for i in range(M):
    maxi, mini = map(int, findMinMax(box))
    box[maxi] -= 1
    box[mini] += 1

maxi, mini = map(int, findMinMax(box))
print(box[maxi]-box[mini])


