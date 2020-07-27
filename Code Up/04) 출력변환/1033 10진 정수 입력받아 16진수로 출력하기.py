# 16진수의 값을 대문자로 받아보자

n = int(input())
hexa = hex(n).upper()

for i in range(len(hexa)):
    if i not in range(0,2):
        print(hexa[i], end="")