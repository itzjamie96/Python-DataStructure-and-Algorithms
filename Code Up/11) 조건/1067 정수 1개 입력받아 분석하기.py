# 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.

n = int(input())

print("minus" if n<0 else "plus")
print("odd" if n%2 else "even")