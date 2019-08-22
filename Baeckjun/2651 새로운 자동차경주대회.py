import sys

K = int(sys.stdin.readline())
N = int(sys.stdin.readline())

locations = list(map(int,['0'] + sys.stdin.readline().split()))
times = list(map(int,['0'] + sys.stdin.readline().split() + ['0']))

for i in range(1, N + 2):
    locations[i] += locations[i - 1]
sum_times = [0 for _ in range(N + 2)]
routes = []
for i in range(1, N + 2):

    temp = []
    for j in range(i - 1, -1, -1):
        if locations[i] - locations[j] > K:
            break
        temp.append(sum_times[j])
    sum_times[i] = min(temp) + times[i]

i = N + 1
while i > 0:
    for j in range(i - 1, -1, -1):
        if sum_times[i] - times[i] == sum_times[j]:
            routes.append(j)
            i = j
            break
routes.pop()
routes.sort()

print(sum_times[N + 1])
print(len(routes))
for value in routes:
    print(value, end=' ')