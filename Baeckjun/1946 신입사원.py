from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def push(nxt):
    global tail
    tail += 1
    stack2[tail] = nxt

def pop():
    global tail
    result = stack2[tail]
    tail -= 1
    return result

for ro in range(int(input())):

    N = int(input())
    heap = []
    for i in range(N):
        x, y = map(int,input().split())
        heappush(heap, (y / x, x, y))
    stack2 = [0] * (N + 1)
    tail = 0
    now = heappop(heap)
    push(now)
    while heap:
        nxt = heappop(heap)
        while tail:
            dx = nxt[1] - stack2[tail][1]
            dy = nxt[2] - stack2[tail][2]
            if dx > 0 and dy > 0:
                break
            if dx < 0 and dy < 0:
                pop()
                if not tail:
                    push(nxt)
                    break
                continue
            else:
                push(nxt)
                break

    print(tail)
