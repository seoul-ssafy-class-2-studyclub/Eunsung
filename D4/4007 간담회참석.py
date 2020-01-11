def heappush(r, heap):
    global length
    heap[length + 1] = r
    length += 1

    child = length
    parent = child // 2

    while parent > 0 and heap[child].c < heap[parent].c:
        heap[child], heap[parent] = heap[parent], heap[child]
        
        child = parent
        parent = child // 2

def heappop(heap):
    global length
    if not length:
        return -1
    result = heap[1]
    heap[1] = heap[length]
    length -= 1

    parent = 1
    child = 2

    if child + 1 <= length:
        if heap[child].c > heap[child + 1].c:
            child += 1
    
    while child <= length and heap[child].c < heap[parent]:

        heap[child], heap[parent] = heap[parent], heap[child]
        
        parent = child
        child = parent * 2

        if child + 1 <= length:
            if heap[child].c > heap[child + 1].c:
                child += 1

    return result
class Route:

    def __init__(self, s, e, c):
        self.nxt = s
        self.e = e
        self.c = c

for ro in range(int(input())):

    N, M, X = map(int,input().split())
    routes = [0] * (M + 5)
    routes_rev = [0] * (M + 5)
    mem = [None] * (N + 5) 
    mem_rev = [None] * (N + 5)
    heap = [None] * (M + 5)
    heap_rev = [None] * (M + 5)
    length = 0
    for m in range(1, M + 1):
        s, e, c = map(int,input().split())
        routes[m] = Route(mem[s], e, c)
        mem[s] = routes[m]
        routes_rev[m] = Route(mem[e], s, c)
        mem[e] = routes_rev[s]
    
    dist = [-1] * (N + 5)
    dist_rev = [-1] * (N + 5)

    dist[X] = 0
    dist_rev[X] = 0
    
    heappush(Route(mem[X], X, 0), heap)

    while length:
        print(heap)
        now = heappop(heap)
        edge = now.nxt
        while edge != None:
            if dist[now.e]:
                edge = edge.nxt
                continue
            
            dist[edge.e] = dist[now.e] + edge.c
            heappush(Route(edge.nxt, edge.e, dist[edge.e]), heap)
            edge = edge.nxt
    print(dist)
