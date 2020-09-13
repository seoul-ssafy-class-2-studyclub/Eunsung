from heapq import heappush, heappop

def solution(food_times, k):
    answer = -1

    foods = {}
    cnt_foods = 0
    for food_time in food_times:
        cnt_foods += 1
        if foods.get(food_time):
            foods[food_time] += 1
        else:
            foods[food_time] = 1
    
    heap = []
    for t, c in foods.items():
        heappush(heap, (t, c))
    length_foods = cnt_foods
    before_t = 0
    while heap:

        t, c = heappop(heap)
        k -= (t - before_t) * cnt_foods

        if k <= 0:
            i = (k % cnt_foods) + 1
            ti = 0
            print(t, c, k)
            if not heap:
                t = t
                if k <= -cnt_foods:
                    break
            else : t, c = heappop(heap)
            for idx in range(length_foods):
                if food_times[idx] == t:
                    ti += 1
                if ti == i:
                    answer = idx + 1
                    break
            if answer >= 0:
                break
        cnt_foods -= c
        before_t = t
        

    return answer

print(solution([3,3,3], 9))