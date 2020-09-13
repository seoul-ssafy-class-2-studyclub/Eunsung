from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    answer = 0

    #인접 리스트 와 인접행렬 구현
    hang_neighbor = [[0] * (n + 1) for _ in range(n + 1)]
    list_neighbor = [[] for _ in range(n + 1)]


    for fare in fares:
        fs, fe, cost = fare
        hang_neighbor[fs][fe] = cost
        hang_neighbor[fe][fs] = cost
        list_neighbor[fe].append(fs)
        list_neighbor[fs].append(fe)

    # 다익스트라 시작
    heap = []
    start = (0, s, s)
    # print('start', start)
    min_cost = 100001 * 200 * 199
    heappush(heap, start)
    # print(hang_neighbor)
    visited = [[min_cost] * (n + 1) for _ in range(n + 1)]

    while heap:

        t_cost, now_a, now_b = heappop(heap)
        if visited[now_a][now_b] <= t_cost:
            continue
        # print(t_cost, now_a, now_b)
        if visited[a][b] <= t_cost:
            break
        
        visited[now_a][now_b] = t_cost
        if now_a == a and now_b == b:
            if min_cost > t_cost:
                min_cost = t_cost
            continue
        
        # 같이있다면 같이 가는 경로
        if now_a == now_b:
            # a가 도착했따면
            if now_a == a:
                for next_b in list_neighbor[now_b]:
                    pay_cost = hang_neighbor[now_b][next_b]
                    t = (t_cost + pay_cost, now_a, next_b)
                    heappush(heap, t)
            elif now_b == b:
                for next_a in list_neighbor[now_a]:
                    pay_cost = hang_neighbor[now_a][next_a]
                    t = (t_cost + pay_cost, next_a, now_b)
                    heappush(heap, t)
            
            else:
                for next_a in list_neighbor[now_a]:
                    pay_cost = hang_neighbor[now_a][next_a]
                    t = (t_cost + pay_cost, next_a, next_a)
                    heappush(heap, t)

        # 나눠지기
            for next_a in list_neighbor[now_a]:
                for next_b in list_neighbor[now_b]:
                    if next_b == next_a:
                        continue
                    pay_cost = hang_neighbor[now_a][next_a] + hang_neighbor[now_b][next_b]
                    t = (t_cost + pay_cost, next_a, next_b)
                    heappush(heap, t)
        # 이미 나눠져있었따면
        else:
            if now_a == a:
                for next_b in list_neighbor[now_b]:
                    pay_cost = hang_neighbor[now_b][next_b]
                    t = (t_cost + pay_cost, now_a, next_b)
                    heappush(heap, t)
            elif now_b == b:
                for next_a in list_neighbor[now_a]:
                    pay_cost = hang_neighbor[now_a][next_a]
                    t = (t_cost + pay_cost, next_a, now_b)
                    heappush(heap, t)
            else:        
                for next_a in list_neighbor[now_a]:
                    for next_b in list_neighbor[now_b]:
                        if next_b == next_a:
                            continue
                        pay_cost = hang_neighbor[now_a][next_a] + hang_neighbor[now_b][next_b]
                        # print('t_cost', t_cost, 'pay_cost', pay_cost, 'now', now_a, now_b, 'ext', next_a, next_b)
                        t = (t_cost + pay_cost, next_a, next_b)
                        heappush(heap, t)
    # print(visited[a][b])
    answer = visited[a][b]
    return answer

solution(6,4,6,2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])