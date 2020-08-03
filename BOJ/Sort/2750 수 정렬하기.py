# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

########버블 정렬을 구현해보자##########

# 몇 개 들어올건지 알려주는 N
N = int(input())

# 한줄씩 들어오는 input을 리스트에 넣자
numList = []
for i in range(N):
    numList.append(int(input()))

def bubbleSort(numList):

    # a boolean to check if the list is already sorted
    # if a swap never happened(swap=False), the list is already sorted
    swap = False

    # 리스트의 모든 인덱스에 대해서 for문을 돌림
    for i in range(len(numList)):

        # i번째 마다 the max among the unsorted is placed at the end
        # since the max will be placed at the end,
        # you just need to loop till right before the last index
        # == 0 ~ len(numList) - i - 1
        for j in range(0, len(numList) - i - 1):

            # if current value is bigger than the next
            if numList[j] > numList[j+1]:
                # swap
                numList[j], numList[j+1] = numList[j+1], numList[j]
                swap = True

        # break the loop if there's no swap
        if swap == False:
            break

    return numList

bubbleSort(numList)

for i in numList:
    print(i)
