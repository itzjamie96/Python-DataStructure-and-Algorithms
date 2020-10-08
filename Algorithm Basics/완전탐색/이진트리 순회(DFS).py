'''
이진트리를 전위순회와 후위순회를 연습
전위순회 출력 : 1 2	4 5	3 6	7
중위순회 출력 : 4 2	5 1	6 3	7
후위순회 출력 : 4 5	2 6	7 3	1
'''
# 전위 순회
def DFS1(v):
    
    if v>7:
        return 
    else:
        print(v, end=' ')    #DFS라는 함수 본연의 일
        DFS1(v*2)    #왼쪽 자식 노드 호출
        DFS1(v*2+1)  #오른쪽 자식 노드 호출

# 중위 순회
def DFS2(v):
    if v>7:
        return 
    # 왼쪽 자식 처리하고 자기 일 하는 방식 = 중위
    else:
        DFS2(v*2)
        print(v, end=' ')
        DFS2(v*2+1)

# 후위 순회
def DFS3(v):
    if v>7:
        return
    else:
        DFS3(v*2)
        DFS3(v*2+1)
        print(v, end=' ')   #자식들 다 처리하고 자기 일 하는 방식 = 후위

if __name__=="__main__":
    DFS1(1)
    print()
    DFS2(1)
    print()
    DFS3(1)