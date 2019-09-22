def combi(arr):
    global cnt
    global result
    if len(arr) == len(num_list):
        cnt += 1
        if cnt == N:
            result = arr
            return  
    if cnt > N:
        return
    for idx in range(length):
        if visited[idx]:
            continue
        visited[idx] = True
        combi(arr + [num_list[idx]])
        visited[idx] = False

num_list = list(map(int, input().strip().split(' ')))
N = int(input())

num_list.sort()
length = len(num_list)
visited = [False] * length

cnt = 0
result = []

combi([])
for num in result:
    print(num, end='')