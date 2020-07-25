# 두 정수(a, b)를 입력받아
# b가 a보다 크거나 같으면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자.

a, b = map(int, input().split())
if b>a or b==a:
    print(1)
else:
    print(0)