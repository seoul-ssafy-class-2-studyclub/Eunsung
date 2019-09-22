from collections import deque
N, K = map(int,input().split())

n_visted = [-1 for _ in range(500001)]
queue = deque([(N, K, 0)])
result = -1

while queue:
    n, k, now = queue.popleft()
    if k > 500000:
        break

    if n == k:
        result = now
        break

    for nxt in [n * 2, n + 1, n - 1]:
        if 0 <= nxt <= 500000 and n_visted[nxt] != now:
            queue.append((nxt, k + now + 1, now + 1))
            n_visted[nxt] = now
    
    if result != -1:
        break

print(result)
    # if n_visted[t % 2][k]:
    #     result = t
    #     break

    # for num in stack[t % 2]:
        
    #     # num = stack[t % 2].pop()
    #     n_visted[t % 2][num] = False

        # if num * 2 <= 500000 and not n_visted[(t + 1) % 2][num * 2]:
        #     stack[(t + 1) % 2].append(num * 2)
        #     n_visted[(t + 1) % 2][num * 2] = True
        #     if num * 2 == k + t + 1:
        #         break
        # if (num + 1) * (2 ** (max_t - t - 1)) > k and num + 1 <= 500000 and not n_visted[(t + 1) % 2][num + 1]:
        #     stack[(t + 1) % 2].append(num + 1)
        #     n_visted[(t + 1) % 2][num + 1] = True
        #     if num + 1 == k + t + 1:
        #         break
        # if (num - 1) * (2 ** (max_t - t - 1)) > k and 0 <= num - 1 and not n_visted[(t + 1) % 2][num - 1]:
        #     stack[(t + 1) % 2].append(num - 1)
        #     n_visted[(t + 1) % 2][num - 1] = True
        #     if num - 1 == k + t + 1:
        #         break

    
    # stack[t % 2] = deque([])
    # t += 1
    # k += t
