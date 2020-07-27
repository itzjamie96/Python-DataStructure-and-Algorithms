# 10진수를 입력받아 8진수(octal)로 출력해보자.

# 2진수 (binary): 0b --> bin(#)
# 8진수 (octal) : 0o --> oct(#)
# 16진수 (hexa) : 0x --> hex(#)

n = int(input())

# oct(n)의 class type = str
# oct(n) = 0o## 형태기 때문에 앞에 0o를 빼고 출력 필요
octal = oct(n)

for i in range(len(octal)):
    if i not in range(0,2):
        print(octal[i], end="")