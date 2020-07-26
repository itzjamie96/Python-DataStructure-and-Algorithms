a, b, c = map(int, input().split())

num = [a,b,c]

for i in num:
    # i%2 == 1 == false
    if i%2:
        print("odd")
    else:
        print("even")