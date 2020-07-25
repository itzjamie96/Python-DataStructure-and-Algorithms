# 입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
# 단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.

a, b = map(int, input().split())
print(a if a>b else b)