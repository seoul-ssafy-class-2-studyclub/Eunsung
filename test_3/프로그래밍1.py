M, C = map(int,input().split())
messages = []
for _ in range(M):
    messages.append(int(input()))
consumers = [[False] * 1001 for _ in range(C)]
max_idx = 0
for idx in range(1, 1001):
    for c in range(C):
        if not consumers[c][idx]:
            gap = messages.pop(0)
            consumers[c][idx: idx + gap] = [True] * gap
            if idx + gap - 1 > max_idx:
                max_idx = idx + gap - 1
        if not messages:
            break
    if not messages:
        break
print(max_idx)