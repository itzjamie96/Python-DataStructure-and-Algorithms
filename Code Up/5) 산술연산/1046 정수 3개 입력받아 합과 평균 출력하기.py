# 합과 평균을 줄을 바꿔 출력한다.
# 평균은 소수점 이하 둘째 자리에서 반올림해서 소수점 이하 첫째 자리까지 출력한다.

a, b, c = map(int, input().split())
sumValue = a+b+c
avgValue = sumValue/3
print(
    sumValue,
    "%.1f"%avgValue,
    sep="\n")