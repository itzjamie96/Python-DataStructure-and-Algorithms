n = int(input())

# 입력받은 정수의 16진수 형태(=0x##)에서
for i in range(len(hex(n))):
    
    # i가 0,1이 아니면
    if i not in range(0,2):
        
        # hex(n)의 그 인덱스 요소를 출력하기
        print(hex(n)[i], end="")