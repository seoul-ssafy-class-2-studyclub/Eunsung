def counting(idx):

    if not relations[idx]:
        return 1
    
    res = 1
    for nxt in relations[idx]:
       res += counting(nxt)
    
    return res


for ro in range(int(input())):
    E, N = map(int,input().split())
    tree = list(map(int,input().split()))
    relations = [[] for _ in range(E + 2)]
    for i in range(E):
        relations[tree[2 * i]].append(tree[2 * i + 1])
    
    print('#%d %d' %(ro + 1, counting(N)))