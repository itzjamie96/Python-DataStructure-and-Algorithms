'''
stack = 2,3,4,1,5
result = []

if result is empty:
    stack[0] vs stack[-1]
        smaller: pop -> append to result

elif stack has only one left:
    check if its bigger than result[-1]
        if yes, pop -> append to result
        else break
else:
    check if stack[0] or stack[-1] is bigger than result[-1]
        if both bigger, compare and find smaller to pop
        elif one, just pop and append that one
        else break

▣ 입력예제
5
2 4 5 1 3

▣ 출력예제
4
LRLL

▣ 입력예제
10
3 2 10 1 5 4 7 8 9 6

▣ 출력예제
3
LRR

'''
import sys
from collections import deque

N = int(sys.stdin.readline())
stack = list(map(int, sys.stdin.readline().split()))
num = []
stack = deque(stack)

result = ''
while stack:
    if len(num) == 0:
        if stack[0] < stack[-1]:
            num.append(stack.popleft())
            result += 'L'
        else:
            num.append(stack.pop())
            result += 'R'

    elif len(stack) == 1:
        if num[-1] < stack[0]:
            num.append(stack.pop())
            result += 'L'
        else:
            break

    else:
        if num[-1] < stack[0] and num[-1] < stack[-1]:
            if stack[0] < stack[-1]:
                num.append(stack.popleft())
                result += 'L'
            else:
                num.append(stack.pop())
                result += 'R'
        elif num[-1] < stack[0]:
            num.append(stack.popleft())
            result += 'L'
        elif num[-1] < stack[-1]:
            num.append(stack.pop())
            result += 'R'
        else:
            break

print(len(num), result, sep='\n')