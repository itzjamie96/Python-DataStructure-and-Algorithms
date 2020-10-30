'''
1~n까지 부분집합 출력하기
- n까지 있는 배열을 만든다 [0,1,2,...,n]
- 어서 그 인덱스의 숫자에 대해 1, 0을 통해 포함여부 확인
- 함수(value)
    - 배열의 value번째 값을 1로 만든다(포함시키기)
    - 그 후 함수(value+1) 진행
    - 끝나면 배열의 value번째 값을 0으로 만든다(포함X)
    - 함수(value+1) 또 진행
- 함수(value)의 value가 n+1이 되면 해당 함수 종료 = 배열에서 값이 1인 애들(포함)만 출력
-'''

def powerset(current):
    if current == n+1:
        for i in range(n+1):
            if visited[i] == 1:
                print(i, end=' ')
        print()

    else:
        visited[current] = 1
        powerset(current+1)

        visited[current] = 0
        powerset(current+1)

n = int(input())
visited = [0]*(n+1)

powerset(1)