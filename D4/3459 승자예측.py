
results = [''] * 100000
for ro in range(int(input())):
    N = int(input())

    n = N + 1
    depth = 0
    while n > 0:
       n = n // 2
       depth += 1

    status = depth % 2 #현재 지는놈. 0: A, 1: B
    flag = depth % 2    
    now = N + 1
    while now > 1:
        if depth % 2 == status:
            if now % 2:
                flag = not status
        else:
            if not now % 2:
                flag = status
        
        now = now // 2
        depth -= 1
    
    result = 'Alice' if flag else 'Bob'
    results[ro] = '#%d %s' %(ro+ 1, result)

re = '\n'.join(results[:ro + 1])
print(re)