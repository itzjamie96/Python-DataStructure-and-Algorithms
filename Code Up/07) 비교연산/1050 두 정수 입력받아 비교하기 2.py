# 두 정수(a, b)를 입력받아
# a와 b가 같으면 1을, 같지 않으면 0을 출력하는 프로그램을 작성해보자.

a, b = map(int, input().split())
if a == b:
    print(1)
else:
    print(0)