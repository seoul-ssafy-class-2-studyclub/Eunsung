for ro in range(int(input())):
    N, M = map(int,input().split())
    containers = list(map(int,input().split()))
    containers.sort(reverse=True)
    trucks = list(map(int,input().split()))
    trucks.sort(reverse=True)

    res = 0
    while trucks:
        tr = trucks.pop(0)
        while containers:
            temp = containers.pop(0)
            if tr >= temp:
                res += temp
                break
            else:
                continue
    
    print('#%d %d' %(ro + 1, res))
    

