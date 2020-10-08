'''
[정다면체]

두 개의 정 N면체와 정M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요. 정답이 여러 개일 경우 오름차순으로 출력합니다.

▣ 입력설명
첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.

▣ 출력설명
첫 번째 줄에 답을 출력합니다.

▣ 입력예제 1
4 6

▣ 출력예제 1
5 6 7
'''
N, M = map(int, input().split())

# 나올 수 있는 면들의 합을 sumList 딕셔너리에 넣어서 각 합이 몇개인지 셈
sumList = dict()

for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(2):

            if i+j in sumList:      #이미 있는 키는 값에 +1
                v = sumList.get(i+j)
                sumList[i+j] = v+1

            else:   #없는 거면 그냥 추가
                sumList[i+j] = 1

# 최대가 여러개일 수 있으니 리스트에 최대 value를 가진 애들을 모두 담겠음
result = []

# value들의 최대를 찾아서
maxi = max(sumList.values())

for k, v in sumList.items():
    if v == maxi:   #value가 최대에 일치하면 key를 result리스트에 추가
        result.append(k)

# 리스트의 모든 내용물 프린트
print(*result, sep=' ')

# print(maxi)