def bubun(res, idx):
    global cnt

    if idx == N:
        if maked.get(res) == None:
            cnt += 1
            maked[res] = 1
        return

    if cache[idx].get(res) != None:
        return
    
    bubun(res + scores[idx], idx + 1)
    bubun(res , idx + 1)

    cache[idx][res] = 1
    return 

for ro in range(int(input())):
    N = int(input())
    scores = list(map(int,input().split()))

    maked = dict()
    cnt = 0
    cache = [{} for _ in range(N)]
    
    bubun(0, 0)
    print('#%d %d' %(ro + 1, cnt))