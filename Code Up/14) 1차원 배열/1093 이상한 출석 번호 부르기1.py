# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.
# 1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.

n = int(input())
numList = list(map(int, input().split()))

countList = []
for i in range(1, 24):
    count = 0
    for num in numList:
        if i==num:
            count +=1
    countList.append(count)

for i in countList:
    print(i, end=" ")