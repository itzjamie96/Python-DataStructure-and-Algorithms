# 1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우,
# 그때까지의 합을 출력한다.

n = int(input())

sumVal = 0
i = 1
while True:
    if sumVal > n or sumVal == n:
        print(sumVal)
        break
    else:
        sumVal += i
        i += 1