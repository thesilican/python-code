def case():
    N = int(input())
    stock = {}
    for _ in range(N):
        M = int(input())
        for _ in range(M):
            inputs = input().split()
            if inputs[0] not in stock:
                stock[inputs[0]] = []
            stock[inputs[0]].append([int(inputs[1]), int(inputs[2])])
    K = int(input())
    total = 0
    for _ in range(K):
        inputs = input().split()
        item = inputs[0]
        amount = int(inputs[1])
        curStock = stock[item]
        curStock.sort(key=lambda x: x[0])
        while amount > 0:
            if curStock[0][1] < 1:
                curStock.pop(0)
            total += curStock[0][0]
            curStock[0][1] -= 1
            amount -= 1
    print(total)


T = int(input())
for i in range(T):
    case()
