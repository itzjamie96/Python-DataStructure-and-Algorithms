# 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
# 출력: 각 자리의 숫자를 분리해 한 줄에 하나씩 [ ]속에 넣어 출력한다.

n = input()

for i in range(len(n)):
    print("[",n[i],"0"*(4-i), "]",sep="")

print()

# fString사용
for i in range(len(n)):
    zero = "0"*(4-i)
    print(f"[{n[i]}{zero}]")
