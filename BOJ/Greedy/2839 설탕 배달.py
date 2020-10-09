import sys

N = int(sys.stdin.readline())

cnt = 0

'''
a = N//5
m = N%5

if m == 0:
    끝!
else
    while a>=0:
        if m이 3의 배수가 아님
            a -= 1
            m += 5
            
        elif (3의 배수)
            cnt += m//3 (봉지 최종 갯수에 m을 3으로 나눈만큼 더하고 끝냄) 
    
    if a== -1:
        cnt = -1
    
'''
a = N//5
m = N%5

if m == 0:
    cnt = a

else:
    while a>= 0:
        if m%3 != 0:
            a -= 1
            m += 5
        else:
            cnt += (m//3) + a
            break

    if a == -1:
        cnt = -1

print(cnt)