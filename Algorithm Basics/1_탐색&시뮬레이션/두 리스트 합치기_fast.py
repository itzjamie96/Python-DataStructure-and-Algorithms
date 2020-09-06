'''
두 리스트 합치기

오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다.
두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다.
네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.

▣ 출력설명
오름차순으로 정렬된 리스트를 출력합니다.

▣ 입력예제 1
3
1 3 5
5
2 3 6 7 9

▣ 출력예제 1
1 2 3 3 5 6 7 9

=> 이미 정렬돼 있는 두 리스트: sort()는 NlogN
=> sort()보다 변수 갯수만큼 8개만큼 반복문을 돌리는게 더 빠름
'''
# 첫번째 리스트
F = int(input())
first = list(map(int, input().split()))

# 두번째 리스트
S = int(input())
second = list(map(int, input().split()))

result = []

i = 0
j = 0

while i<F and j<S:
    if first[i] <= second[j]:
        result.append(first[i])
        i += 1
    else:
        result.append(second[j])
        j += 1

if i<F:
    result = result + first[i:]
elif j<S:
    result = result + second[j:]

print(*result)