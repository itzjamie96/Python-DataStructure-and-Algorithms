'''
0: 현재 속도 유지
1: 가속
2: 감속

a, b가 있으면 a가 command고 b가 속도 였다ㅠ

시작을 0을 둠
a가 0이면 현재 b만큼만 더하기
    1이면 기존 속도 + b
    2이면 기존 속도가 b보다 작으면 기존 속도 = 0
          아니면 기존 속도 - b

이렇게 한 후 더해준다

문제 설명이 아주 구리다! 한국어 공부가 필요하다!
'''
T = int(input())
for tc in range(1, T+1):

    N = int(input())

    total = 0
    speed = 0

    for i in range(N):
        commands = list(map(int, input().split()))

        # 가속일 때
        if commands[0] == 1:
            speed += commands[1]

        elif commands[0] == 2:
            if speed < commands[1]:
                speed = 0
            else:
                speed -= commands[1]

        total += speed

    print('#{} {}'.format(tc, total))
