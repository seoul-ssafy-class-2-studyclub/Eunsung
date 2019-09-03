class Node():
    def __init__(self, value, nxt):
        self.value = value
        self.nxt = nxt
    def __str__(self):
        return '%d' %self.value

for ro in range(int(input())):
    N, M = map(int,input().split())
    
    lists = []
    heads = []
    for i in range(M):
        lists.append(list(map(int,input().split())))

        temp = Node(lists[i][-1], None)
        for j in range(N - 2, -1, -1):
            temp = Node(lists[i][j], temp)
        heads.append(temp)
    
    for i in range(1, M):
        fir = heads[i].value
        p = heads[0]
        while True:
            if p == heads[0] and p.value > fir:
                temp = heads[0]
                heads[0] = heads[i]
                now = heads[i]
                while now.nxt != None:
                    now = now.nxt
                now.nxt = temp
                break

            if p.nxt == None:
                p.nxt = heads[i]
                break

            elif p.nxt.value <= fir:
                p = p.nxt
                continue
                
            elif p.nxt.value > fir:
                temp = p.nxt
                p.nxt = heads[i]
                now = heads[i]
                while now.nxt != None:
                    now = now.nxt
                now.nxt = temp
                break

    result_list = []

    p = heads[0]
    while p.nxt != None:

        result_list.append(p.value)
        p = p.nxt
    result_list.append(p.value)

    result = result_list[N * M - 1: N * M - 11: -1]
    result = list(map(str, result))
    print('#%d %s' %(ro + 1, ' '.join(result)))
            
            



    
    

