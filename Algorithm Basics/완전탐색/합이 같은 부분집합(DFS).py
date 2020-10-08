'''
합이 같은 부분집합

N개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때
두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 “YES"를  출력하고,
그렇지  않으면  ”NO"를 출력하는 프로그램을 작성하세요.
둘로 나뉘는 두 부분집합은 서로소 집합이며, 두 부분집합을 합하면 입력으로 주어진 원래의 집합이 되어야 합니다.
예를 들어 {1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10}으로 두 부분집합의 합이 16으로
같은 경우가 존재하는 것을 알 수 있다.

▣ 입력설명
첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.
두 번째 줄에 집합의 원소 N개가 주어진다. 각 원소는 중복되지 않는다.

▣ 출력설명
첫 번째 줄에 “YES" 또는 ”NO"를 출력한다.

▣  입력예제 1
6
1 3 5 6 7 10

▣ 출력예제 1
YES
'''
def DFS(idx, currentSum):

    global switch

    if switch == 1:
        return

    if idx == N:
        if currentSum == total - currentSum:
            print("YES")
            switch = 1

    else:
        DFS(idx+1, currentSum+arr[idx]) #현재 값을 부분집합에 포함 == 그거까지 합 구하기
        DFS(idx+1, currentSum)  #현재 값을 부분집합에 포함안함 == sum에 합칠필요 없음



N = int(input())
arr = list(map(int, input().split()))
total = sum(arr)

switch = 0  #함수 종료를 위한 flag
result = DFS(0, 0)

if switch == 0:
    print("NO")