"""
주어진 텍스트를 그대로 출력하세요.
#++++
+#+++
++#++
+++#+
++++#

0 #
1 +#
2 ++#
3 +++#
4 ++++#

"""

# +++++ 로 리스트 생성
plus = ["+", "+", "+", "+", "+"]

# 현재 몇번째 row인지 알기 위한 count 변수
# 각 row마다 그 index에 +을 #으로 바꿔줄거임
rowNumber = 0

# 5개의 행
for j in range(5):
    for i in range(len(plus)):
        if i == rowNumber:  #만약 현재 row number와 index가 일치하면
            print(plus[i].replace("+", "#"), end="")    #replace
        else:
            print(plus[i], end="")  #그게 아니면 그냥 프린트
    
    # 잊지말고 증가시켜주기
    rowNumber += 1
    
    print() # 줄바꿈
