'''
- a시 a분, b시 b분 입력받기
- a시 + b시
- a분 + b분
    - 만약 a분+b분이 60초과라면 시+1, a+b분-60
- 13시 부터는 다시 12 빼주는거 잊지말기
'''
T = int(input())
for tc in range(1, T+1):

    h1, m1, h2, m2 = map(int, input().split())

    hour = h1+h2
    if hour > 12:
        hour -= 12

    minutes = m1+m2

    if minutes > 60:
        minutes -= 60
        hour += 1

    print('#{} {} {}'.format(tc, hour, minutes))