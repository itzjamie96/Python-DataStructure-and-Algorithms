'''
문제가 넘 재밌다. 환경에 관심많은 상근이...착해
+ sort를 쓰면 시간초과가 난다! 함수 쓰는 걸 조심해야겠군

1. 나무 N이랑 필요M 입력받기
2. 나무 높이들 입력받기
3. start=0, end=N-1 (인덱스로 갈거임)
4. mid구해서 mid로 자르면 나무 몇미터 나오는지 확인하는 함수 만들기~
5. 함수 결과로 start end 조정
    - M보다 크거나 같으면 답 keep + start 조정
    - M보다 작으면 현재 길이가 너무 긴거니까 end 조정
'''
def cuts(length):
    total = 0
    for tree in trees:
        if length < tree:           #나무가 자르는 길이보다 길어야 계산가능
            total += (tree-length)

    return total

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)
ans = 0

while start <= end:
    mid = (start+end)//2

    if cuts(mid) >= M:
        ans = mid
        start = mid +1
    else:
        end = mid -1

print(ans)