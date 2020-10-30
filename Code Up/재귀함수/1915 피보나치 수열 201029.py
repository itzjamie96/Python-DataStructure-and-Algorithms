'''
N번째 피보나치 구하기
피보나치 수열: 앞에 두개 더한게 그 다음값

1 ~ N까지로 합시다
1에서 점점 더해서 N이 되면 그때 값을 리턴
현재 값 = n-1 + n-2
'''
def fibo(n):
    if n == 1:
        return 1
    elif n==0:
        return 0
    else:
        return fibo(n-1)+fibo(n-2)

n = int(input())

print(fibo(n))