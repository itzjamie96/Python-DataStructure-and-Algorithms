# 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

alphaList = list(map(str, input().split()))

for i in alphaList:
    if i == "q":
        print(i)
        break
    else:
        print(i)