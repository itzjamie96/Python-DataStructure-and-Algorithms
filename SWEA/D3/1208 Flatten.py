def findMin(numList):
    min = numList[0]

    for i in range(1, len(numList)):
        if min > numList[i]:
            min = numList[i]

    return min

def findMax(numList):
    max = numList[0]

    for i in range(1, len(numList)):
        if max < numList[i]:
            max = numList[i]

    return max

for i in range(10):

    dump = int(input())

    numList = list(map(int, input().split()))

    for j in range(dump):

        maxIdx = numList.index(findMax(numList))
        minIdx = numList.index(findMin(numList))

        numList[maxIdx] -= 1
        numList[minIdx] += 1

    print(f"#{i+1} {findMax(numList) - findMin(numList)}")
