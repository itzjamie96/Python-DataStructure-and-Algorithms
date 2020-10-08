import sys

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))

left = 0
right = N-1
lastNum = 0
tmp = []

result = ''

while left <= right:
    if numList[left] > lastNum:
        tmp.append((numList[left], 'L'))

    if numList[right] > lastNum:
        tmp.append((numList[right], 'R'))

    tmp.sort()
    
    # 정렬했는데 아무것도 없다 = 마지막 값보다 다 작은거
    if len(tmp) == 0:   
        break

    else:
        result += tmp[0][1]     # 더 작은 수의 L/R인지 알파벳 붙이기
        lastNum = tmp[0][0]     # 더 작은 수의 숫자 부분을 현재 마지막값으로

        if tmp[0][1] == 'L':
            left += 1
        else:
            right -= 1

    tmp.clear()

print(len(result), result, sep='\n')


