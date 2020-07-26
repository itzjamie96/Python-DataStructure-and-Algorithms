# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
# 1071과 동일, but 조건/반복문 쓰기


numList = list(map(int, input().split()))

# while loop 쓰기 위한 i와 길이
length = len(numList)
i = 0

while i < length:
    if numList[i] == 0:
        break
    else:
        print(numList[i])
        i += 1