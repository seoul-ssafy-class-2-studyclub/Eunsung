from heapq import heappop, heappush

def solution(N, stages):
    answer = []
    
    clears = [0] *(N + 1)
    fail = [0] * (N + 1)

    for stage in stages:

        for i in range(1, N + 1):
            if i == stage:
                fail[i] += 1
            elif i < stage:
                clears[i] += 1
    st = [0] * (N + 1)
    t_answer = []
    answer = [0] * N
    for i in range(1, N + 1):
        if fail[i] + clears[i]:
            st[i] = fail[i] / (fail[i] + clears[i])
        else:
            st[i] = 0
        heappush(t_answer, (-st[i], i))
        
    for i in range(N):
        answer[i] = (heappop(t_answer)[1])
    return answer