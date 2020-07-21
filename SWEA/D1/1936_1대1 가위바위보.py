# a와 b가 가위바위보를 하였다.
# 가위는 1, 바위는 2, 보는 3으로 표현되며 a와 b가 무엇을 냈는지 입력으로 주어진다.
# a와 b중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.
# 입력: 3 2
# 출력: A


# " "를 기준으로 input값 split하기
# .split()은 무조건 문자열에만 해당
# A,B = input().split() = str
# 따라서 정수로 변환하려면 map을 써야함
A, B = map(int, input().split())

if A == 1:
    if B == 2:
        print("B")
    else:
        print("A")
elif A == 2:
    if B == 1:
        print("A")
    else:
        print("B")
elif A == 3:
    if B == 1:
        print("B")
    else:
        print("A")


# 다른 방법
# A가 이기는 경우:
# 가위(1) vs 보(3) / A-B = -2
# 바위(2) vs 가위(1) / A-B = 1
# 보(3) vs 바위(2) / A-B = 1
if A-B == 1 or A-B == -2:
    print("A")
else:
    print("B")