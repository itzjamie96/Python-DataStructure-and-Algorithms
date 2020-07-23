n = input()

# 정수 앞에 0o가 붙어야함
n = "0o"+n

# 진수의 base값을 ,뒤에 인자로 넘겨줌
print(int(n,8))