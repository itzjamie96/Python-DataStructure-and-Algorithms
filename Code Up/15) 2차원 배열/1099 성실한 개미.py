"""
개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
(오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.

10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.

개미가 이동한 경로를 9로 표시해 출력한다.
"""

# 미로 만들기
maze = []
for j in range(10):
    maze.append(list(map(int, input().split())))


# 가로 인덱스를 keep할 변수
# 만약 오른쪽이 벽이면 그 가로좌표 값을 가지고 한칸 아래로 내려가야 하기 때문에 가로 인덱스 keep이 필요함
# 시작은 무조건 2,2 = 인덱스 1,1 이기 때문에 idx의 값은 1부터 시작
idx = 1

# 이중 for문을 break하기 위한 변수
breaker = False

# 0번째 row는 벽이니까 1번째부터 시작
for i in range(1, len(maze)):
    row = maze[i]
    
    # 이중 for문 break을 위한 변수
    if breaker == True:
        break
    else:
        # 가로로 확인
        for j in range(idx, len(row)):

            # 만약 현재 값이 2 == 먹이라면 그 위치도 9로 바꾸고 이중 for문 break
            if row[j] == 2:
                row[j] = 9
                breaker = True
                break

            # 만약 현재 값이 1 == 미로 끝난거니까 이중 for문 break
            elif row[j] == 1:
                breaker = True
                break

            # 만약 오른쪽이 길이거나 먹이라면 우선 현위치 9로 바꾸고 continue
            elif row[j+1] == 0 or row[j+1] == 2:
                row[j] = 9

            # 만약 오른쪽이 벽이라면 현위치 9로 바꾸고 idx값 바꿔주기
            # idx값을 현재 가로인덱스인 j로 바꿔줘야 다음 줄에서도 j 위치에서 시작할 수 있음
            else:
                row[j] = 9
                idx = j
                break


# 미로 결과 프린트
for i in maze:
    print(" ".join(map(str, i)))

