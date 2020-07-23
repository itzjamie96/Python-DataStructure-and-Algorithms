# 16진수니까 앞에 0x
n = "0x"+input()

# 일반 정수로 변환
intN = int(n,16)

# 그걸 8진수로 바꿈
oct = oct(intN)

# 생각해보니 for문이 필요없고 그냥 index 2 뒤부터 slice하면 됐었다!!!!!
# 세상에 이 방법을 까먹다니
print(oct[2:])