'''
- 1 ~ N까지 str형태로 리스트를 만든다
- 현재 값에 3, 6, 9가 포함되어있다면:
    -  현재 값에서 3, 6, 9의 갯수를 카운트
    - '-'*갯수 출력
- 369 아니면 그냥 출력
'''
N = int(input())
nList = [str(i) for i in range(1, N+1)]

for num in nList:
    cnt = 0
    if '3' in num:
        cnt += num.count('3')
    if '6' in num:
        cnt += num.count('6')
    if '9' in num:
        cnt += num.count('9')
    if cnt > 0:
        print('-'*cnt, end=' ')
    else:
        print(num, end=' ')