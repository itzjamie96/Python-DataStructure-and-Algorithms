import sys

N = int(sys.stdin.readline())

# 일단 5키로 봉지에 최대로 담아본다
fives = N//5

# 5키로 봉지에 꽉 채워서 담고 남은 거
left = N%5

# 전체 봉지의 합을 구할 cnt
cnt = 0

# 5키로 봉지를 아예 안쓰는 경우가 있을 때까지 돌려본다
while fives != -1:
    
    # 남은 설탕이 3의 배수면 끝
    if left%3 == 0:
        cnt = fives + left//3
        break
    
    # 남은 설탕이 3의 배수가 아니라면
    else:
        fives -= 1  #5키로 봉지 한개를 빼고
        left += 5   #5키로 만큼 남은 양에 추가해준다

# 중간에 break없이 끝났다 
# = 3키로 봉지로도 딱 채워서 못만든다
# = 딱 떨어지는 경우가 없다
if fives == -1:
    cnt = -1    # 안 되는 경우는 -1 리턴해야함

# 위의 if문에서 걸리지 않았다면 최종 cnt를 출력한다
print(cnt)



