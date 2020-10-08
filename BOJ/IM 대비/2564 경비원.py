'''
[0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
'''

def locate(d, x):
    if d == 1:
        locations[H-1][x-1] = 1
        return (H-1, x-1)
    elif d == 2:
        locations[0][x-1] = 1
        return (0, x-1)
    elif d == 3:
        locations[x-1][0] = 1
        return (x-1, 0)
    elif d == 4:
        locations[x-1][H-1] = 1
        return (x-1, H-1)


def route(startX, startY, findX, findY):
    newX, newY = startX, startY

    # left, down, right
    left = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    # right, down, left
    right = [(0, 1), (-1, 0), (1, 0), (0, -1)]

    l = r = 1
    for i in range(left):

        verti = left[i][0]
        hori = left[i][1]

        currX = startX+verti
        currY = startY+hori

        if 0 <= currX < W and 0 <= currY < H and locations[currX][currY] == 0:
            l += 1
            locations[startX+verti][startY+hori] = 9
            newX = startX+verti
            newY = startY+hori

            if newX == findX and newY == findY:
                return l



W, H = map(int, input().split())

locations = [[0]*W for _ in range(H)]

N = int(input())
stores = []
for _ in range(N):
    d, x = map(int, input().split())
    stores.append((d,x))

# locate 동근
a, b = map(int, input().split())
start = locate(a, b)
# print(start)

# locate stores
positions = []
for d, x in stores:
    positions.append(locate(d, x))

# print(positions)

route(start[0], start[1], positions[0][0], positions[0][1])

# print(*locations, sep='\n')