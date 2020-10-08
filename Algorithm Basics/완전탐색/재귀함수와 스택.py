# 재귀함수와 스택
def DFS(x):
    if x>0:
        DFS(x-1)
        print(x, end=' ')


if __name__=="__main__":
    n = int(input())
    DFS(n)

