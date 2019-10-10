def make_tree(now_idx):
    global cnt

    if now_idx * 2 <= N:
        make_tree(2 * now_idx)
    
    binary_tree[now_idx] = cnt
    cnt += 1

    if now_idx * 2 + 1 <= N:
        make_tree(2 * now_idx + 1)

            
for ro in range(int(input())):
    N = int(input())
    binary_tree = [0] * (N + 1)

    cnt = 1

    make_tree(1)
    # print(binary_tree)
    print('#%d %d %d' %(ro + 1, binary_tree[1] ,binary_tree[N // 2]))