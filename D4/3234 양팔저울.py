def counting(left, right, k, now):

    if left < right:
        return 0

    if k == N:
        return 1
    if cache[now] != -1:
        return cache[now]
    
    res = 0
    for idx in range(N):
        if visited[idx]:
            continue
        visited[idx] = True
        res += counting(left + weights[idx], right, k + 1, now + (1 << (idx + N)))
        res += counting(left, right + weights[idx], k + 1, now + (1 << idx))
        visited[idx] = False

    cache[now] = res
    return res
    

for ro in range(int(input())):
    N = int(input())
    weights = list(map(int,input().split()))
    visited = [False] * N
    cnt = 0
    cache = [-1] * (1 << (N * 2))
    res = counting(0, 0, 0, 0)
    
    print('#%d %d' %(ro + 1, res))