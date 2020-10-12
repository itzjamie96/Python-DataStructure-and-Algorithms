'''
재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다. << ????
ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

숫자는 스택에 넣는다
0이 오면 파압
합을 구한다
'''
import sys

K = int(sys.stdin.readline())
stack = []

for i in range(K):
    current = int(sys.stdin.readline())

    if current == 0:
        stack.pop()
    else:
        stack.append(current)

print(sum(stack))