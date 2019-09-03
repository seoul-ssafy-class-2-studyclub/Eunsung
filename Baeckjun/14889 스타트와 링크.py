def maketeam(start, start_sum, sidx):
    global min_gap

    if len(start) == N // 2:
        link_sum = 0
        link = set(range(N)) - start
        link = list(link)
        for i in range(len(link) - 1):
            for j in range(i + 1, len(link)):
                link_sum += relations[link[i]][link[j]]
                link_sum += relations[link[j]][link[i]]
        temp = abs(start_sum - link_sum)
        if temp < min_gap:
            min_gap = temp
        return
    
    for idx in range(sidx + 1, N):
        future = start_sum
        for player in start:
            future += relations[player][idx]
            future += relations[idx][player]
        
        maketeam(start | {idx}, future, idx)

N = int(input())
relations = []
total_sum = 0
for i in range(N):
    relations.append(list(map(int,input().split())))
    total_sum += sum(relations[i])
min_gap = 999999
for sta in range(N):
    maketeam({sta}, 0, sta)
print(min_gap)