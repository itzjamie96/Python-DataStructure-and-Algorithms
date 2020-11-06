'''
점화식 구하기 = 최종적으로 어떤 경우가 남는지 확인한다
- 가로 길이가 10인 종이와 20인 종이로 만들 수 있는 경우는 총 3가지다
- 10짜리 종이가 끝에 오는 경우 1개, 20짜리 종이가 끝에 오는 경우 2개

'''
def paste(N):
    if N <= 1:
        return 1
    else:
        return paste(N-1) + 2*paste(N-2)

T = int(input())
for tc in range(1, T+1):

    N = int(input())//10

    print('#{} {}'.format(tc, paste(N)))