def solution(n, weak, dist):
    answer = 0
    dist.reverse()
    dp = {}

    def check(start, i, visited_weak):

        for w in weak:
            if start <= w <= start + dist[i]:
                visited_weak = visited_weak | (1 << w)

            if start + dist[i] >= n and 0 <= w <= (start + dist[i]) % n:
                visited_weak = visited_weak | (1 << w)

        if dp.get((visited_weak, num_friends)):
            if dp.get((visited_weak, num_friends)) <= i:
                return False
        if i + 1 == num_friends:
            flag = True
            for w in weak:
                if not visited_weak & (1 << w):
                    flag = False
            return flag
        

        for next_start in weak:
            if visited_weak & (1 << next_start):
                continue
            else:
                if check(next_start, i + 1,  visited_weak):
                    return True
        
        dp[(visited_weak, num_friends)] = i
        return False

    for num_friends in range(1, len(dist) + 1):
        for sw in weak:
            if check(sw, 0,  0):
                return num_friends

    return -1

print("#1")
print(solution(12, [1,5,6,10], [1,2,3,4]))

print("#2")
print(solution(12, [1,3,4,9,10], [3,5,7]))