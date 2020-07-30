"""
하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.

입력 6789

출력 30
"""

n = input()

result = 0
for i in n:
    result += int(i)
print(result)