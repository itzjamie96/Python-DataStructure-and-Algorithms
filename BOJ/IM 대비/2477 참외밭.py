K = int(input())

fruits = []
sides = [0]*5
for _ in range(6):
    a, b = map(int, input().split())
    fruits.append((a, b))
    sides[a] += 1

total = 1
big = 0
small = 0
for i in range(1, 5):
    if sides[i] == 1:
        for j in fruits:
            if j[0] == i:
                total *= j[1]
                break



area = fruits[1][1] * fruits[2][1]

print(K*(total-area))
