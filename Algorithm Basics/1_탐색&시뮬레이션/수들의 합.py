'''
수들의 합

N개의 수로  된  수열  A[1], A[2], …, A[N]  이 있다. 이 수열의  i번째 수부터 j번째 수까지의 합
A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

▣ 입력설명
첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다.
다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다.
각각의 A[x]는 30,000을 넘지 않는 자연수이다.

▣ 출력설명
첫째 줄에 경우의 수를 출력한다.

▣ 입력예제 1
8 3
1 2 1 3 1 1 1 2

▣ 출력예제 1
5

- 연속적인 부분수열의 합이 M과 같은 경우만 카운트 하는거임!
'''
N, M = map(int, input().split())

numList = list(map(int, input().split()))

start = 0   #구역 시작
end = 1   #구역 끝
cnt = 0 #총 갯수를 셀 변수

total = numList[0]  #부분수열들의 합
# total = start ~ end(인덱스 전)까지

while True:

    # 현재까지의 합이 M보다 작을 때
    if total < M:
        # 끝 위치가 아직 N보다 작다면 현재까지의 값을 합해주고 end+1
        if end < N:
            total += numList[end]
            end += 1
        # 끝 위치가 N이면 갈곳이 없으니 break
        else:
            break

    # 현재까지의 합이 M일 때 = 원하는 경우의 수
    elif total == M:
        cnt += 1

        # 새로운 시작지점에서 시작하기 위해 기존의 시작지점값을 빼줌
        # 빼고나면 새로운 시작점의 값이 있을 거임
        total -= numList[start]
        start += 1

    # 현재까지의 합이 M보다 크면 새로운 시퀀스를 찾아봐야함
    # 기존의 시작점을 빼고 새로운 시작점으로 다시 시퀀스 찾기
    else:
        total -= numList[start]
        start += 1

print(cnt)



