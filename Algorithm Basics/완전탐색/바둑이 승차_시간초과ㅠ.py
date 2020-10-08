'''
바둑이 승차(DFS)

철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 그런데 그의 트럭은 Ckg 넘게 태울 수가 없다.
철수는 C를 넘지 않으면서 그의 바둑이들을 가장 많이 태우고 싶다.
N마리의 바둑이와 각 바둑이의 무게 W가 주어지면,
철수가 트럭에 태울 수 있는 가장 무거운 무게를 구하는 프로그램을 작성하세요.


▣ 입력설명
첫 번째 줄에 자연수 C(1<=C<=100,000,000)와 N(1<=N<=30)이 주어집니다. 둘째 줄부터 N마리 바둑이의 무게가 주어진다.

▣ 출력설명
첫 번째 줄에 가장 무거운 무게를 출력한다.

▣ 입력예제 1
259 5
81
58
42
33
61

▣ 출력예제 1
242
'''
# ㅠㅠ 시간초과
# 바둑이들의 부분집합의 합을 구해서 maxi랑 비교 후 더 크면 maxi랑 스왑하기
def DFS(v):

    global maxi

    if v == N+1:
        tmp = []
        for i in range(N):
            if check[i] == 1:
                tmp.append(dogs[i])
        if sum(tmp) < C and sum(tmp)> maxi:
            maxi = sum(tmp)

    else:
        check[v] = 1

        DFS(v+1)
        check[v] = 0
        DFS(v+1)


# 최대 무게, 바둑이 N마리
C, N = map(int, input().split())

# 바둑이들 리스트
dogs = []

# 각 바둑이 무게 입력받아서 리스트에 넣기
for _ in range(N):
    dogs.append(int(input()))

maxi = 0
check = [0] * (N+1)     # 바둑이들의 부분집합 포함여부 확인할 배열
DFS(0)
print(maxi)