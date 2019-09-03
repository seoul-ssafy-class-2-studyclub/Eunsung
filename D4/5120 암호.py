class Node():
    def __init__(self, value, nxt):
        self.value = value
        self.nxt = nxt
    def __str__(self):
        return '%d' %self.value

    
for ro in range(int(input())):
    N, M, K = map(int,input().split())

    first_list = list(map(int,input().split()))

    temp = Node(first_list[-1], None)
    last = temp
    for i in range(N-2, -1, -1):
        temp = Node(first_list[i], temp)
    last.nxt = temp
    head = temp

    now = head
    for _ in range(K):
        for _ in range(M - 1):
            now = now.nxt
        now.nxt = Node(now.value + now.nxt.value, now.nxt)
        now = now.nxt
    
    result_list = []
    p = head
    for _ in range(N + K):
        result_list.append(p.value)
        p = p.nxt
    
    result = result_list[::-1]
    
    print('#%d' %(ro + 1), end = ' ')
    for i in range(len(result)):
        print('%d' %(result[i]), end = ' ')
        if i == 9:
            break
    print('')
    
