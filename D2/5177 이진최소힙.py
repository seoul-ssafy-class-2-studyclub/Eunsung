def replace(now_idx):
    if now_idx // 2 >= 1:
        if binary_tree[now_idx] < binary_tree[now_idx // 2]:
            binary_tree[now_idx], binary_tree[now_idx // 2] = binary_tree[now_idx // 2], binary_tree[now_idx]
            replace(now_idx // 2)

def maketree(now_node):
    global idx
    if now_node > N:
        return
    binary_tree[now_node] = num_list[idx]
    idx += 1
    if now_node // 2 >= 1:
        if binary_tree[now_node] < binary_tree[now_node // 2]:
            replace(now_node)
    maketree(now_node + 1)

def findancestor(now):
    global sums

    if now < 1:
        return
    
    sums += binary_tree[now]
    findancestor(now // 2)


for ro in range(int(input())):
    N = int(input())
    num_list = list(map(int,input().split()))

    binary_tree = [0] * (N + 1)
    idx = 0
    maketree(1)
    sums = 0
    findancestor(N // 2)
    print('#%d %d' %(ro + 1, sums))
