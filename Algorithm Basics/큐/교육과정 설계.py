'''
과목에 for문을 돌린다
필수과목이 있으면 걔만 따로 뽑음
뽑아놓은 거랑 필수과목이랑 똑같으면 YES, 아니면 NO
'''
import sys

course = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
courseList = [sys.stdin.readline().rstrip() for _ in range(N)]

for i in range(N):
    tmp = ''

    for c in courseList[i]:
        if c in course and c not in tmp:
            tmp += c

    if tmp == course:
        print('#{} YES'.format(i+1))
    else:
        print('#{} NO'.format(i + 1))