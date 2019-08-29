for ro in range(1,11):
    N, start_index = map(int,input().split())
    visited = [False for _ in range(101)]
    relations = [[] for _ in range(101)]
    indexs = list(map(int,input().split()))
    result = []
    queue = [(start_index,0)]

    for i in range(N // 2):
        start, end = indexs[2 * i], indexs[2 * i + 1]
        relations[start].append(end)
    before = -1
    visited[start_index] = True
    while True:
        temp = queue.pop(0)

        if temp[1] != before:
            result.append([])
        
        temp_index = temp[0]
        before = temp[1]

        for nxt in relations[temp_index]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            queue.append((nxt, before + 1))
        result[-1].append(temp_index)
        
        if not queue:
            break
    print('#%d %d' %(ro, max(result[-1])))



        
