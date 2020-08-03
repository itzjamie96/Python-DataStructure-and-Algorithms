# 강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.
# 이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.
# 그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.
# 빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.

# 테스트 케이스는 총 10번이다
for n in range(10):

    # 입력될 건물들의 갯수
    T = int(input())

    # 건물들을 입력받아 b(buildings) 리스트에 넣는다
    b = list(map(int, input().split()))

    # 확보된 조망권의 갯수
    result = 0

    # 전체 리스트에서 맨 앞, 뒤 두칸은 아무것도 없기 때문에 2부터 전체 길이-2까지 for문을 돌림
    for i in range(2, len(b) - 1):

        # i번째 건물의 양쪽다 i보다 작을 때
        if b[i - 1] < b[i] and b[i + 1] < b[i]:
            # 더 작은 difference를 keep함
            diff = b[i] - b[i - 1] if b[i] - b[i - 1] < b[i] - b[i + 1] else b[i] - b[i + 1]

            # i번째의 양쪽다 작다면 한칸 더 옆까지 확인해야함
            # i번째의 두칸으로? 양옆까지 i보다 작은지 확인
            if b[i - 2] < b[i] and b[i + 2] < b[i]:

                # 여기서 더 작은 difference를 keep함
                new_diff = b[i] - b[i - 2] if b[i] - b[i - 2] < b[i] - b[i + 2] else b[i] - b[i + 2]

                # 양 옆과 옆옆까지 비교했을 때 더 작은 difference가 조망권 확보된 칸의 갯수
                # result에 더해준다
                if new_diff < diff:
                    result += new_diff
                else:
                    result += diff

        # 애초에 양옆의 건물들이 i번째보다 크면 패쓰
        else:
            continue

    print(f"#{n + 1} {result}")