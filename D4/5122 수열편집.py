class Node():
    def __init__(self, value, nxt):
        self.value = value
        self.nxt = nxt
    def __str__(self):
        return '%d' %self.value
for ro in range(int(input())):
    N, M, L = map(int,input().split())
    first_list = list(map(int,input().split()))

    temp = Node(first_list[-1], None)
    for i in range(N - 2, -1, -1):
        temp = Node(first_list[i], temp)
    head = temp

    for _ in range(M):
        todo = input().split()

        if todo[0] == 'I':
            idx = int(todo[1])
            val = int(todo[2])

            p = head

            for _ in range(idx -1):
                p = p.nxt
            p.nxt = Node(val, p.nxt)
        
        if todo[0] == 'D':
            idx = int(todo[1])

            p = head

            for _ in range(idx -1):
                p = p.nxt
            p.nxt = p.nxt.nxt
        
        else:
            idx = int(todo[1])
            val = int(todo[2])
            p = head
            for _ in range(idx):
                p = p.nxt
            p.value = val
    
    p = head
    
    result = 0
    for _ in range(L):
        if p.nxt == None:
            result = -1
            break
        p = p.nxt
        
    if not result:
        result = p.value
        

    print('#%d %d'%(ro + 1, result))
