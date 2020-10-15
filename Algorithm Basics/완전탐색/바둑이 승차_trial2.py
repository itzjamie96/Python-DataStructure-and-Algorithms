import sys

# 바둑이 무게의 부분집합들을 구해서 최대값 찾기
def checkSum(idx, currentSum, soFar):
    global maxi

    # 지금까지의 누적합 + (전체합-그동안 더한 값=남은 값 최대합)이 현재 maxi보다 작으면
    # 더 볼 필요가 없다. 어짜피 앞으로 더할 값들이 지금 최댓값보다 작으면 뭐하러 더함?
    if currentSum + (total-soFar) < maxi:
        return

    if currentSum > C:
        return

    if idx == N:
        if currentSum > maxi:
            maxi = currentSum

    else:
        checkSum(idx+1, currentSum+dogs[idx], currentSum+dogs[idx])
        checkSum(idx+1, currentSum, currentSum+dogs[idx])



# 몇마리, 무게 입력받기
C, N = map(int, sys.stdin.readline().split())
dogs = []
for i in range(N):
    dogs.append(int(sys.stdin.readline()))

maxi = 0
total = sum(dogs)
checkSum(0, 0, 0)

print(maxi)
