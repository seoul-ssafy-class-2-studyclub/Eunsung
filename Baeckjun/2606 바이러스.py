N = int(input())
M = int(input())
relations = [[] for _ in range(N + 1)]
visited = []
for _ in range(M):
    start_node, end_node = map(int,input().split())
    relations[start_node].append(end_node)
    relations[end_node].append(start_node)

stack = [1]
while True:

    if stack:
        temp = stack.pop()
        if not temp in visited:
            visited.append(temp)
    
    for _ in range(len(relations[temp])):
        stack.append(relations[temp].pop())
    
    if not stack:
        break

print(len(visited) -1)

