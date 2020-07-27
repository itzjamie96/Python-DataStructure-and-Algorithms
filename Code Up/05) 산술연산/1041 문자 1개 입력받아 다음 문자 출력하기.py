# 영문자 한개를 입력받아 그 다음 문자를 출력해보자

# input의 아스키 값을 구한 후 1을 더하면 다음 알파벳의 아스키값
next = ord(input()) + 1

# 문자로 변환
print(chr(next))