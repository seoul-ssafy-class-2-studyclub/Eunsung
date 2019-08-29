for ro in range(int(input())):
    N, M = map(int,input().split())
    temp = list(map(int,input().split()))
    cheese = []
    for i in range(1, M + 1):
        cheese.append([i, temp[i - 1]])
    
    queue = []
    for _ in range(N):
        queue.append(cheese.pop(0))
    
    last_pizza = 0
    while queue:
        pizza = queue.pop(0)
        if pizza[1] // 2 == 0:
            last_pizza = pizza[0]
            if len(cheese) > 0:
                queue.append(cheese.pop(0))
        
        else:
            pizza[1] = pizza[1] // 2
            queue.append(pizza)
    print('#%d %d' %(ro + 1, last_pizza))

