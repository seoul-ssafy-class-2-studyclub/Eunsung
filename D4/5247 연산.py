from collections import deque

for ro in range(int(input())):
    N, M = map(int,input().split())
    visited = [False] * 1000001

    queue = deque()
    queue.append((N, 0))

    while queue:
        num, depth = queue.popleft()
        
        if visited[num]:
            continue
        visited[num] = True

        flag = 0
        for add in [1, -1, num, -10]:
            if num + add < 0 or num + add > 1000000:
                continue

            if num + add == M:
                result = depth + 1
                flag = 1
                break

            queue.append((num + add, depth + 1))
        if flag:
            break
    print('#%d %d' %(ro + 1, result))

