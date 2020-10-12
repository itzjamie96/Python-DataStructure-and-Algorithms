'''
(는 넣는다
)는 파압

다 끝나고 스택에 먼가 남아있으면 NO
아니면 YES
'''
import sys

T = int(sys.stdin.readline())

for t in range(T):
    stack = []
    flag = True

    string = sys.stdin.readline().rstrip()
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(string[i])
        else:
            if len(stack) == 0:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if len(stack) > 0:
            print("NO")
        else:
            print("YES")