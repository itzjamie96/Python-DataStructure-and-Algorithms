def preOrder(n):
    if n >7:
        return
    else:
        print(n, end=' ')
        preOrder(2*n)
        preOrder(2*n+1)

def inOrder(n):
    if n>7:
        return
    else:
        inOrder(2*n)
        print(n, end=' ')
        inOrder(2*n+1)

def postOrder(n):
    if n>7:
        return
    else:
        postOrder(2*n)
        postOrder(2*n+1)
        print(n, end=' ')

preOrder(1)
print()
inOrder(1)
print()
postOrder(1)

'''
1 2 4 5 3 6 7 
4 2 5 1 6 3 7 
4 5 2 6 7 3 1
'''