# 주어진 숫자부터 0까지 순서대로 찍어보세요
# 입력: 8
# 출력: 8 7 6 5 4 3 2 1 0

# N 입력받기
# 그냥 input()으로 받으면 문자열이기 때문에 int로 변환 필수
N = int(input())

# N에서 0까지 -1씩 감소하는 for loop
for i in range(N, -1, -1):
    print(i, end=" ")


print()

# reversed 함수 이용하기
# reversed(range(N))은 N-1부터 시작
for i in reversed(range(N+1)):
    print(i, end=" ")

"""
1. for와 range에서 숫자 감소시키기 = reversed for loop

- range는 기본적으로 1씩 증가함
- 따라서 숫자를 감소시키려면 증가하는 폭을 음수로 지정해주면 됨

EX) 
for i in range(10, 0, -1):    # 10에서 1까지 역순으로 숫자 생성
    print('Hello, world!', i)
    
2. reversed   
reversed(range(횟수))
reversed(range(시작, 끝))
reversed(range(시작, 끝, 증가폭))
"""

