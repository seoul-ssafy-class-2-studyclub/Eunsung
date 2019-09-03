num = []
n = 2
while True:
    res = (n - 1) * (n - 2) // 2 + 1
    num.append(res)
    if res > 10000:
        break
    n += 1

num.insert(0, 0)
num.insert(0, 0)
length = len(num)

# print(num)
for ro in range(int(input())):
    ex = map(int,input().split())
    lo = []

    for goal in ex:
        for i in range(2, length - 1):
            if num[i] <= goal < num[i + 1]:
                break
        dx = goal - num[i]
        lo.append((1 + dx, i - 1 - dx))
    x, y = lo[0][0] + lo[1][0], lo[0][1] + lo[1][1]
    
    n = x + y
    res = (n - 1) * (n - 2) // 2 + x

    print('#%d %d' %(ro + 1, res))


    