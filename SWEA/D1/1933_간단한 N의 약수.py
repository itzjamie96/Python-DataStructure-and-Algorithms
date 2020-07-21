# 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하라

N = int(input())

# range(N) --> 0 ~ N-1까지 = 0 이상 N 미만

# range(1, N+1) = 1 이상 N+1 미만
for i in range(1, N+1):
    if N % i == 0:  # i로 나눴을 때 나머지가 0이라면
        print(i, end=" ")