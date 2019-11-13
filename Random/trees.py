from collections import deque

def bfsearch(tree):
    tree = [tree]
    Q = deque([])
    visited = []
    Q.appendleft([tree[0], [0]])
    while len(Q) > 0:
        v, index = Q.pop()
        if type(v) != type([]):
            for _ in index:
                print('-', end="")
            print(v)
            continue
        for i in range(len(v)):
            sI = index.copy()
            sI.append(i)
            for _ in sI:
                print('-', end="")
            print(v[i])
            if sI not in visited:
                Q.appendleft([v[i], sI])
                visited.append(sI.copy())

Tree = 
bfsearch(Tree)