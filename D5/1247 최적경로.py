def permutation(arr, k, dis):
    global min_dis
        
    if k == N:
        
        dis += abs(lo_list[arr[-1]][0] - lo_list[1][0]) + abs(lo_list[arr[-1]][1] - lo_list[1][1])
        if dis < min_dis:
            min_dis = dis
        return
    
    if dis >= min_dis:
        return

    for idx in range(len(num_list)):
        if visited[idx]:
            continue
        if dis + abs(lo_list[num_list[idx]][0] - lo_list[arr[-1]][0]) + abs(lo_list[num_list[idx]][1] - lo_list[arr[-1]][1]) > min_dis:
            continue
        visited[idx] = True
        permutation(arr + [num_list[idx]], k + 1, dis + abs(lo_list[num_list[idx]][0] - lo_list[arr[-1]][0]) + abs(lo_list[num_list[idx]][1] - lo_list[arr[-1]][1]))
        visited[idx] = False

for ro in range(int(input())):
    N = int(input())
    li = list(map(int,input().split()))
    lo_list = []

    for i in range(N + 2):
        lo_list.append((li[2 * i], li[2 * i + 1]))

    visited = [False for _ in range(N)]

    num_list = list(range(2, N + 2))
    min_dis = 9999999
    permutation([0], 0, 0)

    print('#%d %d' %(ro + 1,min_dis))
