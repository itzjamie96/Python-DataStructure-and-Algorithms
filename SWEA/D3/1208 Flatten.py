'''
- 주어진 횟수동안 max-1, min+1을 수행함
- max-min 리턴
'''

# 직접 min, max의 인덱스를 리턴하는 함수를 짰다
def findMinMax(numList):
    min = max = numList[0]
    minIdx, maxIdx = 0, 0
    for i in range(1, len(numList)):
        if min > numList[i]:
            min = numList[i]
            minIdx = i
        if max < numList[i]:
            max = numList[i]
            maxIdx = i
    return (minIdx, maxIdx)


for tc in range(1, 11):
    dump = int(input())
    numList = list(map(int, input().split()))
    for j in range(dump):
        minIdx = findMinMax(numList)[0]
        maxIdx = findMinMax(numList)[1]
        numList[minIdx] += 1
        numList[maxIdx] -= 1

    minmax = findMinMax(numList)
    print(f"#{tc} {numList[minmax[1]] - numList[minmax[0]]}")
