# 1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가,
# 입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력한다.

n = int(input())

sumValue = 0
i = 1

while True:
    if sumValue==n or sumValue>n:
        # 지난 회차에서 이미 i += 1 이 실행됐기 때문에
        # 실제 우리가 원하는 값은 i-1
        print(i-1)
        break
    else:
        sumValue += i
        i += 1

