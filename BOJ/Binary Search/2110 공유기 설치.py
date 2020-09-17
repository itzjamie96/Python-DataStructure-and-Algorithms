'''
공유기 부자 도현이 부럽네
나도 이분탐색 오른쪽 왼쪽 쓸거임

1. N, C 입력받기
2. N만큼 숫자 들어오는거 리스트로 받기 => 정렬
3. left = 1, right = 최대
4. 거리가 mid일 때 놓을 수 있는 공유기 갯수 구하는 함수 만들기
    - 현재값 - 처음 공유기 값 >= mid면 cnt+1
5. 함수 결과가 C 이상이면 left 조정, 반대면 right 조정
'''
def countWifi(distance):
    current = 0
    cnt = 1

    for i in range(1, N):
        if homes[i] - homes[current] >= distance:
            cnt += 1
            current = i

    return cnt

N, C = map(int, input().split())
homes = []
for _ in range(N):
    homes.append(int(input()))

homes.sort()

left = 1
right = homes[N-1]
ans = 0
while left<=right:
    mid = (left+right)//2

    if countWifi(mid) >= C:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)


