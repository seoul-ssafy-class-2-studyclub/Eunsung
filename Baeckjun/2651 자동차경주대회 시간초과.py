import sys

def dfs(now_location, now_times, k, ls):
    if now_location == N + 1:
        return now_times, ls


    if cache[now_location].get((now_times,k)) != None:
        return cache[now_location].get((now_times,k))
        
    if k < locations[now_location + 1]:
        cache[now_location][(now_times,k)] = (sum_time, [])
        return (sum_time, [])
    res = []
    distance = 0
    for next in range(now_location + 1, N + 2):
        distance += locations[next]

        if distance > k:
            break
        res.append(dfs(next, now_times, k - distance, ls))

        res.append(dfs(next, now_times + times[next], K, ls+[next]))

    res.sort(key=lambda x: x[0])
    result = (sum_time,[]) if len(res) == 0 else res[0]

    cache[now_location][(now_times,k)] = result

    return result


K = int(sys.stdin.readline())
N = int(sys.stdin.readline())

locations = list(map(int,['0'] + sys.stdin.readline().split()))
times = list(map(int,['0'] + sys.stdin.readline().split() + ['0']))
sum_time = sum(times)
cache = [{} for _ in range(N + 1)]
result = dfs(0,0,K,[])

print(result[0])
print(len(result[1]))
for value in result[1]:
    print(value, end = ' ')

# print(cache[0])
# print(cache)

