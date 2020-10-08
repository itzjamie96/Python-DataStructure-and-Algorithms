
W, H = map(int, input().split())

# print(W//2)
N = int(input())
locations = []
for _ in range(N):
    a, b = map(int, input().split())
    locations.append((a,b))

Dir, loc = map(int, input().split())

Len = 0
for i in range(len(locations)):
    d = locations[i][0]
    x = locations[i][1]

    # 상점이 가로로 있을 때
    if d == 1 or d == 2:
        # 나랑 같은 선상이면 오른쪽인지 왼쪽인지 판단후 거리 구하기
        if d == Dir:
            if loc<x:
                Len += (x - loc)
            else:
                Len += (loc - x)

        # 내 위쪽에 있다면 중간 기준으로 오른쪽/왼쪽 중 뭐가 더 가까운지 판단
        else:
            if x < W//2:
                Len += (loc + H + x)
            else:
                Len += (W - loc + H + W - x)
    
    # 3이면 내 왼쪽
    elif d == 3:
        if x <= H//2:
            Len += (loc + W-x)
        else:
            Len += (loc+x)
    else:
        if x <= H//2:
            Len += (W - loc + W-x)
        else:
            Len += (loc+x)
print(Len)
