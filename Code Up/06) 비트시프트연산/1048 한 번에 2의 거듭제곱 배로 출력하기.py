# 정수 2개(a, b)를 입력받아 a를 2^b배 곱한 값으로 출력해보자.
# 예시
# int a=1, b=10;
# printf("%d", a << b); //2^10 = 1024 가 출력된다.

a, b = map(int, input().split())
print(a << b )