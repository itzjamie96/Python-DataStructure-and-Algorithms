'''
영식이랑 성원이는 어디서 나온 이름..? 넘나 한국적...

1. K개 입력받는 걸 리스트에 넣음
2. 최대값을 찾아서 그걸 end로 설정
    - start는 1부터. 0은 길이가 될 수 없으니까
3. mid 길이로 잘랐을 때 몇개가 나올 수 있는지 숫자세는 함수 만들기
    - 길이//mid 를 cnt에 누적시켜준 후 cnt 리턴!
4. 만약 나온 갯수가 N보다 작으면 지금 자른 길이가 너무 길어서 N개만큼 못나온거
    - 그럼 길이를 줄여봐야하니까 end 조정
5. 만약 N보다 같거나 크면 start+1해서 하나씩 좁혀가기 = 최대 랜선 구하는 거니까
'''
# 잘라서 갯수 몇개 나오는지 확인하는 함수
def cuts(length):
    cnt = 0
    for i in lines:
        cnt += i // length
    return cnt

K, N =  map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

start = 1
end = max(lines)
ans = 0
while start <= end:
    mid = (start+end)//2

    if cuts(mid) < N:
        end = mid - 1

    else:
        ans = mid
        start = mid+1

print(ans)
