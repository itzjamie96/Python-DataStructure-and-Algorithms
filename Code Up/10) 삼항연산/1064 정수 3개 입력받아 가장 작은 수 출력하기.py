# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.

a, b, c = map(int, input().split())

# 파이썬의 삼항연산은 if else 두개 만 가능하기 때문에
# 미리 두 정수를 비교해 놓는다
n = a if a<b else b
print(n if n<c else c)