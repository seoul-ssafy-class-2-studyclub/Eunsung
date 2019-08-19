cham = int(input())

locations = []
x = y = 0
for i in range(6):
    see, length = map(int,input().split())
    if see == 1:
        x += length
    elif see == 2:
        x -= length
    elif see == 3:
        y -= length
    else:
        y += length
    locations.append((x,y))
    
first = 0
second = 0
for i in range(5):
    first += locations[i][0] * locations[i+1][1]
    second += locations[i][1] * locations[i+1][0]
result = abs(first - second) // 2

print(cham*result)

