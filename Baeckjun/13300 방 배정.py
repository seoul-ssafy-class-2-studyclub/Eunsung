N, K =  map(int,input().split())

girls = [0 for _ in range(7)]
boys = [0 for _ in range(7)]
for i in range(N):
    s, y = map(int,input().split())
    if s:
        boys[y] += 1
    else:
        girls[y] += 1
# print(boys)
# print(girls)

rooms = 0
for i in range(1, 7):
    if girls[i]:
        rooms += ((girls[i] - 1) // K) + 1
    
    if boys[i]:
        rooms += ((boys[i] - 1) // K) + 1
    # print(rooms)

print(rooms)