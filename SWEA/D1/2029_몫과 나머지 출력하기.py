"""
2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.
[제약 사항]
각 수는 1이상 10000이하의 정수이다.

[입력]
3  <-- test case T
9 2
15 6
369 15

[출력]
#1 4 1
#2 2 3
#3 24 9
"""
# Test Case
T = int(input())

# 결과물 keep하고 출력할 리스트
result = []

for i in range(T):
    # 우선 a와 b를 입력받음
    a, b = map(int, input().split())

    # 몫과 나머지 얻기 = divmod(a,b)
    qu, re = divmod(a,b)

    # 얻은 몫과 나머지를 f-string을 이용해 결과 리스트에 넣어줌
    result.append(f"#{i+1} {qu} {re}")

for i in result:
    print(i)