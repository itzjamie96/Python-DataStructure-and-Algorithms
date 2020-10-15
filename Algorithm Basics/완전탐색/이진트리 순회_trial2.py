# 전위순회: me first - left - right
def preOrder(N):
    if N > 7:
        return
    else:
        print(N, end=' ')
        preOrder(N*2)
        preOrder(N*2+1)

# 중위순회: left - me - right
def inOrder(N):
    if N > 7:
        return
    else:
        inOrder(N*2)
        print(N, end=' ')
        inOrder(N*2+1)

#후위순회: left-right-me
def postOrder(N):
    if N > 7:
        return
    else:
        postOrder(N*2)
        postOrder(N*2+1)
        print(N, end=' ')

preOrder(1)
print()
inOrder(1)
print()
postOrder(1)