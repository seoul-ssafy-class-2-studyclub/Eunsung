for ro in range(int(input())):
    N, M, L = map(int,input().split())
    binary_tree = [0] * (N + 1)
    sons = []
    for _ in range(M):
        node, val = map(int,input().split())
        binary_tree[node] = val
        sons.append(node)
    
    while sons:
        now_node = sons.pop(0)
        if now_node % 2:
            continue
        
        sums = binary_tree[now_node] if now_node + 1 > N else binary_tree[now_node] + binary_tree[now_node + 1]
        if now_node // 2 >= 1:
            binary_tree[now_node // 2] = sums
            sons.append(now_node // 2)
    
    # print(binary_tree)
    print('#%d %d' %(ro + 1, binary_tree[L]))