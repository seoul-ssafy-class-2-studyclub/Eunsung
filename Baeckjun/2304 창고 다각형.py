N = int(input())

sticks = []
for i in range(N):
    sticks.append(tuple(map(int,input().split())))

max_height = 0
max_height_index = 0
max_index = 0
for k in range(N):
    if max_height < sticks[k][1]:
        max_height = sticks[k][1]
        max_height_index = sticks[k][0]

    if max_index < sticks[k][0]:
        max_index = sticks[k][0]
container = [0 for i in range(max_index+1)]

for i in range(N):
    container[sticks[i][0]] = sticks[i][1]

square = 0
temp_max = 0
for i in range(max_height_index):
    if temp_max < container[i]:
        temp_max = container[i]
    square += temp_max
temp_max = 0
for i in range(max_index, max_height_index-1, -1):
    if temp_max < container[i]:
        temp_max = container[i]
    square += temp_max
print(max_height_index)
print(container)
print(square)

