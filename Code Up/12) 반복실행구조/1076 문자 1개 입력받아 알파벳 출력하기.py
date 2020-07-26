# 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.
# f가 입력되면 a~f까지 출력

# input alphabet
alpha = input()

# ascii of a
a = ord("a")

# the end of the loop = alpha's ascii +1
end = ord(alpha) + 1

for i in range(a, end):
    print(chr(i), end=" ")

