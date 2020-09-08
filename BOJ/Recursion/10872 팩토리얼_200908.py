def factorial(N):
    # 지영아..팩토리얼 0은 1이야...잊지마.....
    if N==1 or N==0:
        return 1

    else:
        return N*factorial(N-1)

N = int(input())
print(factorial(N))
