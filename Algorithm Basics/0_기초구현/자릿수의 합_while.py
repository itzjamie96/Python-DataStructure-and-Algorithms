'''
[자릿수의 합]

N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력     하는 프로그램을 작성하세요. 각  자연수의  자릿수의  합을  구하는  함수를  def  digit_sum(x)를  꼭 작성해서 프로그래밍 하세요.

▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그  다음  줄에  N개의  자연수가  주어진다. 각 자연수의 크기는 10,000,000를 넘지 않는다.

▣ 출력설명
자릿수의 합이 최대인 자연수를 출력한다.

▣  입력예제 1
3
125 15232 97

▣  출력예제 1
97
'''
# 각 자릿수의 합을 리턴하는 함수
def digit_sum(num):
    sum = 0
    while num>0:
        sum += num % 10     #1의 자리수 얻기
        num = num // 10     #1의 자릿수 이외 남은 애들 다시 num에 넣어주기

    return sum

N = int(input())
Ns = list(map(int, input().split()))

max = -2147000000
for i in Ns:
    total = digit_sum(i)

    if total > max:
        max = total
        ans = i

print(i)