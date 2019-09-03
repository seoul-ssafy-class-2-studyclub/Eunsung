class Node():
    def __init__(self, value, nxt):
        self.value = value
        self.nxt = nxt
    def __str__(self):
        return '%d' %self.value

for ro in range(int(input())):
    N, M, L = map(int,input().split())
    first_list = list(map(int,input().split()))
    todo_list = []
    for _ in range(M):
        todo_list.append(tuple(map(int,input().split())))
    
    temp = Node(first_list[-1], None)
    for i in range(N - 2, -1, -1):
        temp = Node(first_list[i], temp)
    head = temp

    for idx, val in todo_list:
    
        now = head
        for _ in range(idx - 1):
            now = now.nxt
        
        now.nxt = Node(val, now.nxt)

    p = head
    for _ in range(L):
        p = p.nxt

    print('#%d %d' %(ro + 1, p.value))
    

