def dis(me, shop):
    if me[0] == shop[0] and (me[0] == 0 or me[0] == w) :
        return abs(me[1] - shop[1])
    elif me[1] == shop[1] and (me[1] == 0 or me[1] == h):
        return abs(me[0] - shop[0])
    elif set([me[0], shop[0]]) == {0, w}:
        return min(2 * h - me[1] - shop[1], me[1] + shop[1]) + w
    elif set([me[1], shop[1]]) == {0, h}:
        return min(2 * w - me[0] - shop[0], me[0] + shop[0]) + h
    else:
        return abs(me[0] - shop[0]) + abs(me[1] - shop[1])
    
w, h = map(int,input().split())
shops = []
N = int(input())
for i in range(N + 1):
    line, distance = map(int,input().split())
    if line == 1:
        shops.append((distance, h))
    elif line == 2:
        shops.append((distance, 0))
    elif line == 3:
        shops.append((0, h - distance))
    else:
        shops.append((w, h - distance))

me = shops.pop()
count = 0
for shop in shops:
    count += dis(me, shop)
print(count)
